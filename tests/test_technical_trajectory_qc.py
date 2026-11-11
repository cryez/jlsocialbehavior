import tempfile
import unittest
from pathlib import Path

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

from functions.technical_trajectory_qc import (
    TechnicalTrajectoryAccumulator,
    add_technical_qc_flags,
    analyze_trajectory_file_cached,
    plot_si_with_technical_flags,
    technical_cache_path,
)


class TechnicalTrajectoryQCTests(unittest.TestCase):
    def make_accumulator(self, requested_frames, max_jump=20.0):
        return TechnicalTrajectoryAccumulator(
            n_fish=1,
            centres_px=np.array([0.0]),
            px_per_mm=1.0,
            dish_radius_mm=50.0,
            max_jump_mm_per_frame=max_jump,
            requested_frames=requested_frames,
        )

    def test_all_valid_and_strict_jump_boundary(self):
        accumulator = self.make_accumulator(requested_frames=3)
        accumulator.start_segment()
        accumulator.add_chunk(
            np.array([[[0.0, 0.0]], [[20.0, 0.0]], [[40.1, 0.0]]])
        )

        result = accumulator.result()

        self.assertEqual(result.missing_position_count.tolist(), [0])
        self.assertEqual(result.outside_dish_count.tolist(), [0])
        self.assertEqual(result.implausible_jump_count.tolist(), [1])
        self.assertAlmostEqual(result.implausible_jump_fraction[0], 1 / 3)

    def test_missing_short_read_outside_and_overlapping_jump(self):
        accumulator = self.make_accumulator(requested_frames=6)
        accumulator.start_segment()
        accumulator.add_chunk(
            np.array(
                [
                    [[0.0, 0.0]],
                    [[np.nan, 0.0]],
                    [[60.0, 0.0]],
                    [[0.0, 0.0]],
                ]
            )
        )

        result = accumulator.result()

        self.assertEqual(result.observed_frames, 4)
        self.assertEqual(result.missing_position_count.tolist(), [3])
        self.assertEqual(result.outside_dish_count.tolist(), [1])
        self.assertEqual(result.implausible_jump_count.tolist(), [1])
        self.assertAlmostEqual(result.missing_position_fraction[0], 0.5)
        self.assertAlmostEqual(result.outside_dish_fraction[0], 1 / 6)
        self.assertAlmostEqual(result.implausible_jump_fraction[0], 1 / 6)

    def test_chunk_boundary_is_compared_but_segment_boundary_is_not(self):
        continuous = self.make_accumulator(requested_frames=2)
        continuous.start_segment()
        continuous.add_chunk(np.array([[[0.0, 0.0]]]))
        continuous.add_chunk(np.array([[[21.0, 0.0]]]))

        separated = self.make_accumulator(requested_frames=2)
        separated.start_segment()
        separated.add_chunk(np.array([[[0.0, 0.0]]]))
        separated.start_segment()
        separated.add_chunk(np.array([[[21.0, 0.0]]]))

        self.assertEqual(continuous.result().implausible_jump_count.tolist(), [1])
        self.assertEqual(separated.result().implausible_jump_count.tolist(), [0])

    def test_missing_frame_is_not_bridged_for_jump_detection(self):
        accumulator = self.make_accumulator(requested_frames=3)
        accumulator.start_segment()
        accumulator.add_chunk(
            np.array([[[0.0, 0.0]], [[np.nan, np.nan]], [[40.0, 0.0]]])
        )

        self.assertEqual(accumulator.result().implausible_jump_count.tolist(), [0])

    def test_fraction_flag_is_strictly_greater_than_threshold(self):
        threshold = 0.001
        qc_table = pd.DataFrame(
            {
                "experiment_key": [1, 1, 1],
                "QTLID": ["below", "equal", "above"],
            }
        )
        technical_results = pd.DataFrame(
            {
                "experiment_key": [1, 1, 1],
                "QTLID": ["below", "equal", "above"],
                "test_fraction": [
                    np.nextafter(threshold, -np.inf),
                    threshold,
                    np.nextafter(threshold, np.inf),
                ],
            }
        )

        flagged = add_technical_qc_flags(
            qc_table,
            technical_results,
            {"test": {"column": "test_fraction", "label": "Test fraction"}},
            threshold,
        )

        self.assertEqual(
            flagged["test_technical_flag"].tolist(),
            [False, False, True],
        )

    def test_si_plot_uses_only_technical_qc_flags(self):
        data = pd.DataFrame(
            {
                "experiment_label": ["experiment-a"] * 4,
                "si": [-1.5, -0.2, 0.3, 1.5],
                "missing_position_technical_flag": [True, False, False, False],
                "outside_dish_technical_flag": [False, True, False, False],
                "implausible_jump_technical_flag": [False, False, False, True],
                "technical_qc_flag": [True, True, False, True],
            }
        )
        technical_metrics = {
            "missing_position": {
                "label": "Missing-position fraction",
                "color": "#B2182B",
                "marker": "X",
                "marker_size": 150,
                "abbreviation": "missing",
            },
            "outside_dish": {
                "label": "Outside-dish fraction",
                "color": "#EF8A62",
                "marker": "P",
                "marker_size": 170,
                "abbreviation": "outside",
            },
            "implausible_jump": {
                "label": "Implausible-jump fraction",
                "color": "#762A83",
                "marker": "*",
                "marker_size": 205,
                "abbreviation": "jump",
            },
        }

        def add_plot_positions(frame, order):
            positioned = frame.copy()
            positioned["_plot_x"] = np.linspace(-0.12, 0.12, len(positioned))
            return positioned

        figure, axis = plot_si_with_technical_flags(
            data=data,
            technical_metrics=technical_metrics,
            experiment_order=lambda frame: ["experiment-a"],
            add_plot_positions=add_plot_positions,
            unflagged_color="#808080",
            summary_color="#202020",
            figure_dpi=72,
            figure_height=5,
            final_si_y_limits=(-1, 1),
        )
        try:
            figure.canvas.draw()
            self.assertEqual(
                axis.get_title(),
                "Shoaling index with full-frame technical QC flags",
            )
            self.assertEqual(
                [text.get_text() for text in axis.get_legend().get_texts()],
                [
                    "all fish",
                    "Missing-position fraction (technical)",
                    "Outside-dish fraction (technical)",
                    "Implausible-jump fraction (technical)",
                ],
            )
            annotations = "\n".join(text.get_text() for text in axis.texts)
            self.assertIn("tech=3", annotations)
            self.assertIn("missing=1", annotations)
            self.assertIn("outside=1", annotations)
            self.assertIn("jump=1", annotations)
            self.assertIn("Hidden below: 1 points (1 technical-QC flagged)", annotations)
            self.assertIn("Hidden above: 1 points (1 technical-QC flagged)", annotations)
            self.assertNotIn("qc=", annotations.casefold())
            self.assertNotIn("review", annotations.casefold())
        finally:
            plt.close(figure)

    def test_cache_round_trip_and_jump_setting_key(self):
        repository_root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory(dir=repository_root) as temp_dir:
            temp_dir = Path(temp_dir)
            trajectory_path = temp_dir / "trajectory.npy"
            np.save(
                trajectory_path,
                np.array([[[0.0, 0.0]], [[5.0, 0.0]], [[30.0, 0.0]]]),
            )
            arguments = {
                "cache_dir": temp_dir / "cache",
                "use_cache": True,
                "trajectory_path": trajectory_path,
                "segments": ((0, 3),),
                "n_fish": 1,
                "fps": 30,
                "centres_px": np.array([0.0]),
                "px_per_mm": 1.0,
                "dish_radius_mm": 50.0,
                "max_jump_mm_per_frame": 20.0,
                "chunk_frames": 1,
            }

            calculated, cache_path, was_cached = analyze_trajectory_file_cached(**arguments)
            loaded, loaded_path, loaded_from_cache = analyze_trajectory_file_cached(**arguments)
            alternate_path, _ = technical_cache_path(
                cache_dir=arguments["cache_dir"],
                trajectory_path=trajectory_path,
                segments=arguments["segments"],
                n_fish=1,
                fps=30,
                centres_px=np.array([0.0]),
                px_per_mm=1.0,
                dish_radius_mm=50.0,
                max_jump_mm_per_frame=35.0,
            )

            self.assertFalse(was_cached)
            self.assertTrue(loaded_from_cache)
            self.assertEqual(cache_path, loaded_path)
            self.assertNotEqual(cache_path, alternate_path)
            self.assertEqual(calculated.implausible_jump_count.tolist(), [1])
            self.assertTrue(
                np.array_equal(
                    calculated.implausible_jump_count,
                    loaded.implausible_jump_count,
                )
            )


if __name__ == "__main__":
    unittest.main()
