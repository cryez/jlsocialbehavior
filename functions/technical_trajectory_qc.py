"""Full-frame technical quality metrics for multi-fish trajectories."""

from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import warnings

from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


TECHNICAL_QC_CACHE_SCHEMA = "technical-trajectory-qc-v1"


@dataclass(frozen=True)
class TechnicalTrajectoryResult:
    """Per-fish counts and fractions from one requested trajectory selection."""

    requested_frames: int
    observed_frames: int
    missing_position_count: np.ndarray
    outside_dish_count: np.ndarray
    implausible_jump_count: np.ndarray
    missing_position_fraction: np.ndarray
    outside_dish_fraction: np.ndarray
    implausible_jump_fraction: np.ndarray


class TechnicalTrajectoryAccumulator:
    """Accumulate technical trajectory counts without retaining complete recordings."""

    def __init__(
        self,
        n_fish,
        centres_px,
        px_per_mm,
        dish_radius_mm,
        max_jump_mm_per_frame,
        requested_frames,
    ):
        self.n_fish = int(n_fish)
        self.centres_px = np.asarray(centres_px, dtype=float)
        self.px_per_mm = float(px_per_mm)
        self.dish_radius_mm = float(dish_radius_mm)
        self.max_jump_mm_per_frame = float(max_jump_mm_per_frame)
        self.requested_frames = int(requested_frames)

        if self.n_fish < 1:
            raise ValueError("n_fish must be positive.")
        if self.centres_px.shape != (self.n_fish,):
            raise ValueError("centres_px must contain one crop centre per fish.")
        if not np.isfinite(self.px_per_mm) or self.px_per_mm <= 0:
            raise ValueError("px_per_mm must be positive and finite.")
        if not np.isfinite(self.dish_radius_mm) or self.dish_radius_mm <= 0:
            raise ValueError("dish_radius_mm must be positive and finite.")
        if (
            not np.isfinite(self.max_jump_mm_per_frame)
            or self.max_jump_mm_per_frame <= 0
        ):
            raise ValueError("max_jump_mm_per_frame must be positive and finite.")
        if self.requested_frames <= 0:
            raise ValueError("requested_frames must be positive.")

        self.observed_frames = 0
        self.missing_position_count = np.zeros(self.n_fish, dtype=np.int64)
        self.outside_dish_count = np.zeros(self.n_fish, dtype=np.int64)
        self.implausible_jump_count = np.zeros(self.n_fish, dtype=np.int64)
        self._previous_xy_mm = None
        self._previous_valid = None

    def start_segment(self):
        """Prevent jump comparisons across noncontiguous requested segments."""
        self._previous_xy_mm = None
        self._previous_valid = None

    def add_chunk(self, raw_xy_px):
        """Accumulate one consecutive chunk shaped ``(frames, fish, 2)``."""
        raw_xy_px = np.asarray(raw_xy_px, dtype=float)
        if raw_xy_px.ndim != 3 or raw_xy_px.shape[1:] != (self.n_fish, 2):
            raise ValueError(
                f"raw_xy_px must have shape (frames, {self.n_fish}, 2)."
            )
        if raw_xy_px.shape[0] == 0:
            return

        valid = np.isfinite(raw_xy_px).all(axis=2)
        self.missing_position_count += (~valid).sum(axis=0)
        self.observed_frames += raw_xy_px.shape[0]

        xy_mm = (
            raw_xy_px - self.centres_px[np.newaxis, :, np.newaxis]
        ) / self.px_per_mm
        radial_distance = np.sqrt(np.square(xy_mm).sum(axis=2))
        self.outside_dish_count += (
            valid & (radial_distance > self.dish_radius_mm)
        ).sum(axis=0)

        if self._previous_xy_mm is not None:
            boundary_valid = self._previous_valid & valid[0]
            boundary_distance = np.sqrt(
                np.square(xy_mm[0] - self._previous_xy_mm).sum(axis=1)
            )
            self.implausible_jump_count += (
                boundary_valid
                & (boundary_distance > self.max_jump_mm_per_frame)
            )

        if raw_xy_px.shape[0] > 1:
            pair_valid = valid[:-1] & valid[1:]
            frame_distance = np.sqrt(
                np.square(np.diff(xy_mm, axis=0)).sum(axis=2)
            )
            self.implausible_jump_count += (
                pair_valid
                & (frame_distance > self.max_jump_mm_per_frame)
            ).sum(axis=0)

        self._previous_xy_mm = xy_mm[-1].copy()
        self._previous_valid = valid[-1].copy()

    def result(self):
        """Return counts and fractions, including out-of-bounds sampling loss."""
        if self.observed_frames > self.requested_frames:
            raise ValueError("Observed frames exceed requested frames.")

        unavailable_frames = self.requested_frames - self.observed_frames
        missing_count = self.missing_position_count + unavailable_frames
        denominator = float(self.requested_frames)
        return TechnicalTrajectoryResult(
            requested_frames=self.requested_frames,
            observed_frames=self.observed_frames,
            missing_position_count=missing_count.copy(),
            outside_dish_count=self.outside_dish_count.copy(),
            implausible_jump_count=self.implausible_jump_count.copy(),
            missing_position_fraction=missing_count / denominator,
            outside_dish_fraction=self.outside_dish_count / denominator,
            implausible_jump_fraction=self.implausible_jump_count / denominator,
        )


def _normalize_segments(segments):
    normalized = tuple((int(start), int(stop)) for start, stop in segments)
    if not normalized or any(start < 0 or stop <= start for start, stop in normalized):
        raise ValueError("segments must contain positive start-inclusive/stop-exclusive ranges.")
    return normalized


def analyze_trajectory_file(
    trajectory_path,
    segments,
    n_fish,
    centres_px,
    px_per_mm,
    dish_radius_mm,
    max_jump_mm_per_frame,
    chunk_frames=50_000,
):
    """Read requested full-resolution segments and calculate technical metrics."""
    trajectory_path = Path(trajectory_path)
    segments = _normalize_segments(segments)
    chunk_frames = int(chunk_frames)
    if chunk_frames < 1:
        raise ValueError("chunk_frames must be positive.")

    requested_frames = sum(stop - start for start, stop in segments)
    accumulator = TechnicalTrajectoryAccumulator(
        n_fish=n_fish,
        centres_px=centres_px,
        px_per_mm=px_per_mm,
        dish_radius_mm=dish_radius_mm,
        max_jump_mm_per_frame=max_jump_mm_per_frame,
        requested_frames=requested_frames,
    )

    if trajectory_path.suffix.casefold() == ".npy":
        raw_array = np.load(trajectory_path, mmap_mode="r")
        if raw_array.ndim != 3 or raw_array.shape[1] < n_fish or raw_array.shape[2] < 2:
            raise ValueError("Trajectory array does not contain the requested fish x/y data.")
        for start, stop in segments:
            accumulator.start_segment()
            available_stop = min(stop, raw_array.shape[0])
            for chunk_start in range(start, available_stop, chunk_frames):
                chunk_stop = min(chunk_start + chunk_frames, available_stop)
                accumulator.add_chunk(
                    np.asarray(raw_array[chunk_start:chunk_stop, :n_fish, :2], dtype=float)
                )
        return accumulator.result()

    with trajectory_path.open("r", encoding="utf-8") as handle:
        first_value = handle.readline().lstrip()
    if first_value.startswith("("):
        raise ValueError("Old Bonsai tuple format is not supported by the technical QC reader.")
    header_rows = 1 if first_value.startswith("X") else 0
    xy_columns = [column for fish in range(n_fish) for column in (fish * 3, fish * 3 + 1)]

    for start, stop in segments:
        accumulator.start_segment()
        try:
            reader = pd.read_csv(
                trajectory_path,
                header=None,
                sep=r"\s+",
                usecols=xy_columns,
                skiprows=start + header_rows,
                nrows=stop - start,
                chunksize=chunk_frames,
            )
            for chunk in reader:
                values = chunk.to_numpy(dtype=float)
                accumulator.add_chunk(values.reshape(values.shape[0], n_fish, 2))
        except pd.errors.EmptyDataError:
            continue

    return accumulator.result()


def technical_cache_path(
    cache_dir,
    trajectory_path,
    segments,
    n_fish,
    fps,
    centres_px,
    px_per_mm,
    dish_radius_mm,
    max_jump_mm_per_frame,
):
    """Return the independent technical-QC cache path and its complete key."""
    trajectory_path = Path(trajectory_path)
    try:
        raw_mtime = trajectory_path.stat().st_mtime
    except OSError:
        raw_mtime = None
    cache_key = {
        "schema": TECHNICAL_QC_CACHE_SCHEMA,
        "trajectory_path": str(trajectory_path),
        "raw_mtime": raw_mtime,
        "segments": [list(segment) for segment in _normalize_segments(segments)],
        "n_fish": int(n_fish),
        "fps": float(fps),
        "centres_px": np.asarray(centres_px, dtype=float).tolist(),
        "px_per_mm": float(px_per_mm),
        "dish_radius_mm": float(dish_radius_mm),
        "max_jump_mm_per_frame": float(max_jump_mm_per_frame),
    }
    digest = hashlib.sha1(
        json.dumps(cache_key, sort_keys=True, default=str).encode("utf-8")
    ).hexdigest()[:12]
    return Path(cache_dir) / f"technical_qc_{digest}.npz", cache_key


def analyze_trajectory_file_cached(
    cache_dir,
    use_cache,
    trajectory_path,
    segments,
    n_fish,
    fps,
    centres_px,
    px_per_mm,
    dish_radius_mm,
    max_jump_mm_per_frame,
    chunk_frames=50_000,
):
    """Load or calculate one experiment's independent technical-QC result."""
    cache_path, cache_key = technical_cache_path(
        cache_dir=cache_dir,
        trajectory_path=trajectory_path,
        segments=segments,
        n_fish=n_fish,
        fps=fps,
        centres_px=centres_px,
        px_per_mm=px_per_mm,
        dish_radius_mm=dish_radius_mm,
        max_jump_mm_per_frame=max_jump_mm_per_frame,
    )
    if use_cache and cache_path.exists():
        with np.load(cache_path, allow_pickle=False) as cached:
            result = TechnicalTrajectoryResult(
                requested_frames=int(cached["requested_frames"]),
                observed_frames=int(cached["observed_frames"]),
                missing_position_count=cached["missing_position_count"].astype(np.int64),
                outside_dish_count=cached["outside_dish_count"].astype(np.int64),
                implausible_jump_count=cached["implausible_jump_count"].astype(np.int64),
                missing_position_fraction=cached["missing_position_fraction"].astype(float),
                outside_dish_fraction=cached["outside_dish_fraction"].astype(float),
                implausible_jump_fraction=cached["implausible_jump_fraction"].astype(float),
            )
        return result, cache_path, True

    result = analyze_trajectory_file(
        trajectory_path=trajectory_path,
        segments=segments,
        n_fish=n_fish,
        centres_px=centres_px,
        px_per_mm=px_per_mm,
        dish_radius_mm=dish_radius_mm,
        max_jump_mm_per_frame=max_jump_mm_per_frame,
        chunk_frames=chunk_frames,
    )
    if use_cache:
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        np.savez_compressed(
            cache_path,
            requested_frames=np.asarray(result.requested_frames),
            observed_frames=np.asarray(result.observed_frames),
            missing_position_count=result.missing_position_count,
            outside_dish_count=result.outside_dish_count,
            implausible_jump_count=result.implausible_jump_count,
            missing_position_fraction=result.missing_position_fraction,
            outside_dish_fraction=result.outside_dish_fraction,
            implausible_jump_fraction=result.implausible_jump_fraction,
            meta_json=np.asarray(json.dumps(cache_key, sort_keys=True, default=str)),
        )
    return result, cache_path, False


def collect_qtl_technical_qc(
    summary_sample_table,
    selections,
    experiments,
    animal_numbers_for_experiment,
    resolve_trajectory_scale,
    expected_n_fish,
    fps,
    cache_dir,
    use_cache,
    max_jump_mm_per_frame,
):
    """Collect independent full-frame technical metrics for QTL experiment-fish rows."""
    results = []
    for _, experiment_row in experiments.iterrows():
        experiment_key = experiment_row["experiment_key"]
        expected_samples = summary_sample_table.loc[
            summary_sample_table["experiment_key"].eq(experiment_key),
            ["anNr", "QTLID"],
        ]
        if expected_samples.empty:
            continue

        try:
            matching_selections = selections.loc[
                selections["experiment_key"].eq(experiment_key)
            ]
            if len(matching_selections) != 1:
                raise ValueError(
                    "Expected one shared trajectory selection; "
                    f"found {len(matching_selections)}."
                )
            selection = matching_selections.iloc[0]
            animal_numbers = animal_numbers_for_experiment(experiment_row)
            n_fish = len(animal_numbers)
            if n_fish != expected_n_fish:
                raise ValueError(f"Expected {expected_n_fish} animal IDs, found {n_fish}.")

            centres_px, px_per_mm, dish_radius_mm, _ = resolve_trajectory_scale(
                experiment_row,
                n_fish,
            )
            technical_result, cache_path, cache_hit = analyze_trajectory_file_cached(
                cache_dir=cache_dir,
                use_cache=use_cache,
                trajectory_path=str(experiment_row["txtPath"]),
                segments=selection["segments"],
                n_fish=n_fish,
                fps=fps,
                centres_px=centres_px,
                px_per_mm=px_per_mm,
                dish_radius_mm=dish_radius_mm,
                max_jump_mm_per_frame=max_jump_mm_per_frame,
            )
            if technical_result.observed_frames < technical_result.requested_frames:
                warnings.warn(
                    f'{experiment_row.get("folder", experiment_key)} supplied '
                    f"{technical_result.observed_frames} of "
                    f"{technical_result.requested_frames} requested full-resolution frames."
                )

            experiment_metrics = pd.DataFrame(
                {
                    "anNr": np.asarray(animal_numbers, dtype=int),
                    "technical_requested_frames": technical_result.requested_frames,
                    "technical_observed_frames": technical_result.observed_frames,
                    "missing_position_count": technical_result.missing_position_count,
                    "outside_dish_count": technical_result.outside_dish_count,
                    "implausible_jump_count": technical_result.implausible_jump_count,
                    "missing_position_fraction": technical_result.missing_position_fraction,
                    "outside_dish_fraction": technical_result.outside_dish_fraction,
                    "implausible_jump_fraction": technical_result.implausible_jump_fraction,
                    "technical_cache_hit": cache_hit,
                    "technical_cache_path": str(cache_path),
                    "technical_qc_error": "",
                }
            )
            experiment_metrics = (
                experiment_metrics.merge(
                    expected_samples,
                    on="anNr",
                    how="inner",
                    validate="one_to_one",
                ).drop(columns="anNr")
            )
            experiment_metrics["experiment_key"] = experiment_key
            results.append(experiment_metrics)
        except Exception as exc:
            message = str(exc)
            warnings.warn(
                "Technical trajectory QC could not be calculated for "
                f'{experiment_row.get("folder", experiment_key)}: {message}'
            )
            failed = expected_samples[["QTLID"]].copy()
            failed["experiment_key"] = experiment_key
            failed["technical_requested_frames"] = np.nan
            failed["technical_observed_frames"] = np.nan
            for column in (
                "missing_position_count",
                "outside_dish_count",
                "implausible_jump_count",
                "missing_position_fraction",
                "outside_dish_fraction",
                "implausible_jump_fraction",
            ):
                failed[column] = np.nan
            failed["technical_cache_hit"] = False
            failed["technical_cache_path"] = ""
            failed["technical_qc_error"] = message
            results.append(failed)

    if not results:
        raise ValueError("No experiment-fish rows were available for technical QC.")
    technical_results = pd.concat(results, ignore_index=True)
    if technical_results.duplicated(["experiment_key", "QTLID"]).any():
        raise AssertionError("Technical QC results contain duplicate experiment-fish rows.")
    return technical_results


def add_technical_qc_flags(qc_table, technical_results, metric_definitions, threshold):
    """Merge independent metrics and add strict upper-threshold technical flags."""
    threshold = float(threshold)
    if not np.isfinite(threshold) or not 0 <= threshold <= 1:
        raise ValueError("threshold must be finite and from 0 to 1.")

    flagged = qc_table.merge(
        technical_results,
        on=["experiment_key", "QTLID"],
        how="left",
        validate="one_to_one",
    )
    fraction_columns = [info["column"] for info in metric_definitions.values()]
    flag_columns = []
    for metric_name, metric_info in metric_definitions.items():
        flag_column = f"{metric_name}_technical_flag"
        flagged[flag_column] = flagged[metric_info["column"]].gt(threshold).fillna(False)
        flag_columns.append(flag_column)

    flagged["technical_qc_flag"] = flagged[flag_columns].any(axis=1)
    flagged["technical_qc_missing_flag"] = flagged[fraction_columns].isna().any(axis=1)

    def reason_text(row):
        return "; ".join(
            metric_info["label"] + " > threshold"
            for metric_name, metric_info in metric_definitions.items()
            if row[f"{metric_name}_technical_flag"]
        )

    flagged["technical_qc_reasons"] = flagged.apply(reason_text, axis=1)
    return flagged


def plot_technical_qc_distributions(
    data,
    metric_definitions,
    threshold,
    experiment_order,
    add_plot_positions,
    summary_color,
    figure_dpi,
):
    """Plot full-frame technical fractions for every experiment-fish sample."""
    order = experiment_order(data)
    positioned = add_plot_positions(data, order)
    fig_width = max(13, 0.8 * len(order) + 3)
    fig, axes = plt.subplots(
        len(metric_definitions),
        1,
        figsize=(fig_width, 14),
        dpi=figure_dpi,
        sharex=True,
        squeeze=False,
    )
    axes = axes.ravel()

    for ax, metric_info in zip(axes, metric_definitions.values()):
        value_column = metric_info["column"]
        finite = positioned.loc[positioned[value_column].notna()]
        ax.scatter(
            finite["_plot_x"],
            finite[value_column],
            s=30,
            color=metric_info["color"],
            alpha=0.5,
            edgecolor="white",
            linewidth=0.35,
            zorder=2,
        )
        for x_position, experiment_label in enumerate(order):
            values = pd.to_numeric(
                data.loc[data["experiment_label"].eq(experiment_label), value_column],
                errors="coerce",
            ).dropna()
            if values.empty:
                continue
            q1, median, q3 = np.percentile(values, [25, 50, 75])
            ax.errorbar(
                x_position,
                median,
                yerr=np.array([[median - q1], [q3 - median]]),
                fmt="D",
                markersize=4.5,
                color=summary_color,
                ecolor=summary_color,
                elinewidth=1.2,
                capsize=3,
                zorder=4,
            )
        ax.axhline(
            threshold,
            color=metric_info["color"],
            linestyle="--",
            linewidth=1.5,
            label=f"strict flag cutoff > {threshold:g}",
        )
        ax.set_yscale("symlog", linthresh=threshold, linscale=1)
        ax.set_ylim(bottom=0)
        ax.set_ylabel(metric_info["label"])
        ax.legend(frameon=False, loc="upper right")
        sns.despine(ax=ax)

    axes[-1].set_xticks(np.arange(len(order)))
    axes[-1].set_xticklabels(order, rotation=90)
    axes[-1].set_xlabel("Experiment")
    fig.suptitle("Full-frame technical trajectory QC by experiment", fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.98])
    return fig, axes


def plot_si_with_standard_and_technical_flags(
    data,
    qc_metrics,
    qc_markers,
    technical_metrics,
    experiment_order,
    add_plot_positions,
    unflagged_color,
    summary_color,
    figure_dpi,
    figure_height,
    final_si_y_limits=None,
):
    """Plot SI with unchanged standard flags and independent technical overlays."""
    order = experiment_order(data)
    positioned = add_plot_positions(data, order)
    complete_si = positioned.loc[positioned["si"].notna()].copy()
    fig_width = max(11, 0.9 * len(order) + 3)
    fig, ax = plt.subplots(figsize=(fig_width, figure_height), dpi=figure_dpi)
    ax.scatter(
        complete_si["_plot_x"],
        complete_si["si"],
        s=38,
        color=unflagged_color,
        alpha=0.58,
        edgecolor="white",
        linewidth=0.45,
        zorder=2,
    )
    sns.pointplot(
        data=complete_si,
        x="experiment_label",
        y="si",
        order=order,
        color=summary_color,
        errorbar="sd",
        linestyle="-",
        markers="D",
        capsize=0.12,
        ax=ax,
    )

    for metric_name, metric_info in qc_metrics.items():
        marker, marker_size = qc_markers[metric_name]
        metric_rows = complete_si.loc[complete_si[f"{metric_name}_outlier_flag"]]
        ax.scatter(
            metric_rows["_plot_x"],
            metric_rows["si"],
            s=marker_size,
            marker=marker,
            facecolors="none",
            edgecolors=metric_info["color"],
            linewidths=1.5,
            zorder=5,
        )
    for metric_name, metric_info in technical_metrics.items():
        metric_rows = complete_si.loc[complete_si[f"{metric_name}_technical_flag"]]
        ax.scatter(
            metric_rows["_plot_x"],
            metric_rows["si"],
            s=metric_info["marker_size"],
            marker=metric_info["marker"],
            facecolors="none",
            edgecolors=metric_info["color"],
            linewidths=1.8,
            zorder=6,
        )

    size_missing = complete_si.loc[complete_si["animal_size_missing_flag"]]
    ax.scatter(
        size_missing["_plot_x"],
        size_missing["si"],
        s=132,
        marker="X",
        color="#7A3D00",
        linewidths=1.2,
        zorder=7,
    )
    for x_position, experiment_label in enumerate(order):
        experiment_data = data.loc[data["experiment_label"].eq(experiment_label)]
        annotations = [
            (1.24, f'qc={int(experiment_data["qc_outlier_flag"].sum())}', summary_color, True),
            (1.205, f'tech={int(experiment_data["technical_qc_flag"].sum())}', "#4D004B", True),
        ]
        annotations.extend(
            (
                1.17 - 0.035 * index,
                f'{info["abbreviation"]}='
                f'{int(experiment_data[f"{name}_technical_flag"].sum())}',
                info["color"],
                False,
            )
            for index, (name, info) in enumerate(technical_metrics.items())
        )
        for y_position, label, color, bold in annotations:
            ax.text(
                x_position,
                y_position,
                label,
                transform=ax.get_xaxis_transform(),
                ha="center",
                va="bottom",
                fontsize=7.2 if bold else 6.8,
                fontweight="bold" if bold else "normal",
                color=color,
            )

    legend_handles = [
        Line2D(
            [0], [0], marker="o", linestyle="none",
            markerfacecolor=unflagged_color, markeredgecolor="white",
            label="all fish", markersize=7,
        )
    ]
    for metric_name, metric_info in qc_metrics.items():
        marker, _ = qc_markers[metric_name]
        legend_handles.append(
            Line2D(
                [0], [0], marker=marker, linestyle="none", markerfacecolor="none",
                markeredgecolor=metric_info["color"], markeredgewidth=1.5,
                label=metric_info["label"], markersize=8,
            )
        )
    for metric_info in technical_metrics.values():
        legend_handles.append(
            Line2D(
                [0], [0], marker=metric_info["marker"], linestyle="none",
                markerfacecolor="none", markeredgecolor=metric_info["color"],
                markeredgewidth=1.8,
                label=metric_info["label"] + " (technical)", markersize=9,
            )
        )
    legend_handles.append(
        Line2D(
            [0], [0], marker="X", linestyle="none",
            markerfacecolor="#7A3D00", markeredgecolor="#7A3D00",
            label="Animal size missing", markersize=8,
        )
    )

    ax.axhline(0, color="0.35", linestyle=":", linewidth=1)
    ax.set_xlabel("Experiment")
    ax.set_ylabel("Shoaling index")
    if final_si_y_limits is not None:
        y_limits = tuple(map(float, final_si_y_limits))
        ax.set_ylim(*y_limits)
        below = np.isfinite(complete_si["si"]) & complete_si["si"].lt(y_limits[0])
        above = np.isfinite(complete_si["si"]) & complete_si["si"].gt(y_limits[1])
        combined_review = complete_si["qc_review_flag"] | complete_si["technical_qc_flag"]
        ax.text(
            0.02,
            0.98,
            f"Hidden below: {int(below.sum())} points "
            f"({int((below & combined_review).sum())} review flagged)\n"
            f"Hidden above: {int(above.sum())} points "
            f"({int((above & combined_review).sum())} review flagged)",
            transform=ax.transAxes,
            ha="left",
            va="top",
            fontsize=8,
            bbox={"facecolor": "white", "alpha": 0.85, "edgecolor": "none"},
        )
    ax.set_title(
        "Shoaling index with standard and full-frame technical QC flags",
        y=1.30,
        pad=0,
    )
    ax.tick_params(axis="x", rotation=90)
    ax.legend(
        handles=legend_handles,
        title="QC overlay",
        frameon=False,
        bbox_to_anchor=(1.01, 1),
        loc="upper left",
    )
    sns.despine(ax=ax)
    fig.tight_layout()
    return fig, ax
