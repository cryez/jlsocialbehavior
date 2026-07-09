# Recent Changes - Notebook Figure Workflows

Append meaningful completed changes here.

### 2026-07-09 - Movement heatmap comments

- Slice goal: Explain the trajectory movement heatmap analysis and its outlier metrics in-place.
- Passes completed: Updated `Analyses/ShoalingTrajectoryGrid_2026.ipynb`.
- What changed: Added notebook markdown and code comments defining the movement-density binning, shared color scale, `movement_z_mad` formula, `movement_z_mad_abs` ranking, and all displayed metrics-table columns.
- Rerun implications: Documentation/comment-only change; rerun the movement heatmap cell only to view the clarified notebook text alongside refreshed outputs.
- Validation performed: Parsed the notebook JSON and compiled all code cells with Python `ast`.

### 2026-07-09 - Trajectory movement heatmap grid

- Slice goal: Add an absolute movement-density heatmap version of the 5x7 trajectory grid for outlier individual screening.
- Passes completed: Updated `Analyses/ShoalingTrajectoryGrid_2026.ipynb`.
- What changed: The notebook now bins frame-to-frame path length into shared-scale per-fish arena heatmaps, annotates each subplot with distance-per-minute and robust MAD z-score, displays a movement outlier table, and saves PNG/PDF heatmaps plus a metrics CSV.
- Rerun implications: No raw-data or summary rerun required; rerun the trajectory-grid notebook cells after loading a trajectory window to refresh the displayed heatmap and saved movement metrics.
- Validation performed: Parsed the notebook JSON, checked all notebook code cells with Python `ast`, and smoke-rendered the movement heatmap helper on dummy 35-fish trajectories with a deliberately high-movement outlier.

### 2026-07-07 - Trajectory-grid genotype labels

- Slice goal: Add each fish's genotype to the 5x7 raw trajectory grid.
- Passes completed: Updated `Analyses/ShoalingTrajectoryGrid_2026.ipynb`.
- What changed: The notebook now loads the selection animal metadata workbook, maps plotted animal IDs to `AllAn.genotype`, prints the genotype vector, and adds a genotype line to each fish subplot title.
- Rerun implications: No raw-data or summary rerun required; rerun the trajectory-grid notebook cells to refresh the displayed and saved PNG/PDF.
- Validation performed: Parsed the notebook JSON, checked all notebook code cells with Python `ast`, and smoke-rendered the grid helper on dummy trajectories with genotype labels.

### 2026-07-07 - Fast trajectory-grid notebook

- Slice goal: Add an independent, frequently runnable 5x7 raw trajectory grid for selected 35-fish experiments.
- Passes completed: Added `Analyses/ShoalingTrajectoryGrid_2026.ipynb` and registered it in the notebook stage map.
- What changed: The notebook uses the slim selection `processingSettings.csv` as an experiment index, reads only requested raw x/y columns for a selected time window, caches parsed windows as compressed `.npz`, and saves 5x7 trajectory grids as PNG/PDF.
- Rerun implications: No summary or neighborhood-map rerun required; rerun the new notebook after editing experiment selection, time window, stride, or cache controls.
- Validation performed: Parsed the notebook JSON and checked all notebook code cells with Python `ast`.

### 2026-07-07 - Neighborhood-map alternative grid row spacing

- Slice goal: Prevent overlapping y-axis labels in the optional alternative-grouping neighborhood-map grids.
- Passes completed: Updated `Analyses/ShoalingNeighborhoodMaps_2026.ipynb`.
- What changed: `plot_group_summary` now accepts optional row padding for tight layout, and the final optional alternative-grouping cell uses larger row padding for the 24-row grid plots.
- Rerun implications: No data rerun required; rerun the grouped-map plotting cells to refresh the displayed and saved PDFs.
- Validation performed: Parsed the notebook JSON, checked all notebook code cells with Python `ast` after skipping IPython magic lines, and smoke-rendered `plot_group_summary` on dummy map data with `row_h_pad=2.8` while intercepting PDF writes.

### 2026-07-06 - Neighborhood-map notebook cache isolation

- Slice goal: Keep neighborhood-map summaries and maps in a notebook-specific processing cache instead of reusing slim-selection summary CSVs.
- Passes completed: Updated `Analyses/ShoalingNeighborhoodMaps_2026.ipynb`, `documentation_cr/neighborhood_map_analysis.md`, and `USER_GUIDE.md`.
- What changed: The notebook now points `ProcessingDir` and `processingSettings_neighborhood_maps.csv` to a `neighborhood_maps` subfolder, keeps `PROCESSING_MISSING_ONLY=True`, and removes the stale warning about slim summaries causing map skips.
- Rerun implications: First neighborhood-map processing in the new cache regenerates summary CSVs and `MapData.npy` files for selected experiments; later runs with `MissingOnly=True` skip experiments whose notebook-specific summaries already exist.
- Validation performed: Parsed notebook JSON, checked code-cell syntax, and statically checked cache paths, `PROCESSING_MISSING_ONLY`, and stale warning removal.

### 2026-07-06 - Neighborhood-map notebook

- Slice goal: Add a focused notebook and human guide for neighborhood-density map analysis using processed selection data.
- Passes completed: Added `Analyses/ShoalingNeighborhoodMaps_2026.ipynb`, documented the workflow in `documentation_cr/neighborhood_map_analysis.md`, and linked the new entrypoint from `USER_GUIDE.md` and the notebook stage map.
- What changed: The notebook can filter selected experiments by year, line, genotype, lineSet, or folder; discovers notebook-specific `*_siSummary*.csv` and `*MapData.npy` files; writes a separate map-specific processing settings CSV; loads neighbor-density maps; exports file/row/group summaries; and saves real, shifted-control, and difference map figures.
- Rerun implications: Neighborhood-map summaries and `MapData.npy` files live in the notebook-specific processing cache; selected experiments can be rerun with `SaveNeighborhoodMaps = 1`.
- Validation performed: Parsed the notebook JSON and checked all notebook code cells with Python `ast` after skipping IPython magic lines.

### 2026-06-30 - Mixed/separate start-date filter

- Slice goal: Move the mixed-vs-separate notebook experiment date filter into the top settings cell.
- Passes completed: Added `FILTER_START_DATE = '2026-01-01'` and changed metadata filtering to include experiments dated on or after that cutoff.
- What changed: `Analyses/ShoalingMixedvsSeparateDotEpisodes.ipynb` now uses `info_filtered` for processing-table construction instead of the hard-coded 2026 year filter.
- Rerun implications: Rerun the notebook from the settings and metadata cells after changing `FILTER_START_DATE`; no pipeline rerun is required just to validate the source change.
- Validation performed: Parsed the notebook JSON, checked all code-cell syntax, confirmed stale 2026 filter source patterns are gone, and confirmed `prepare_processing_table` receives `info_filtered`.

### 2026-06-29 - QTL SI correlation annotation overlap

- Slice goal: Remove the hidden/stacked label under the `R^2` annotation in the lineSet-split SI correlation grid.
- Passes completed: Added a local genotype list for the grid and offset each per-genotype `R^2` label vertically inside `Analyses/ShoalingQTLMappingAnalysis_2026.ipynb`.
- What changed: Multiple genotype annotations no longer draw at the exact same axes position; when more than one genotype is plotted, each `R^2` label is prefixed by genotype.
- Rerun implications: No data rerun required; rerun the lineSet correlation cell to refresh the displayed output.
- Validation performed: Parsed the notebook JSON, checked all notebook code cells with Python `ast` after skipping IPython magic lines, and smoke-rendered the lineSet plotting cell on dummy two-genotype data to confirm each panel has separated `R^2` label positions.

### 2026-06-29 - QTL SI correlations by lineSet thresholds

- Slice goal: Make the lineSet-split SI correlation plot run without depending on the preceding plot cell and draw red dotted threshold guides.
- Passes completed: Removed the `previous_corr_axis_limits` dependency from `Analyses/ShoalingQTLMappingAnalysis_2026.ipynb` and hard-coded the grid thresholds locally.
- What changed: The lineSet grid now plots shoaling index against average speed, animal size, and thigmotaxis distance; average-speed panels draw red dotted guides at `1` and `10`, and thigmotaxis panels draw red dotted guides at `10` and `30`.
- Rerun implications: No data rerun required; rerun the lineSet correlation cell to refresh the displayed output.
- Validation performed: Parsed the notebook JSON, checked all notebook code cells with Python `ast` after skipping IPython magic lines, and smoke-ran the lineSet plotting cell alone on dummy data with a noninteractive Matplotlib backend.

### 2026-06-29 - QTL lineSet correlation x-axis range

- Slice goal: Set the lineSet-split correlation plot x-axis range to `-0.2` through `1`.
- Passes completed: Added a shared `ax.set_xlim(-0.2, 1)` inside the lineSet subplot loop in `Analyses/ShoalingQTLMappingAnalysis_2026.ipynb`.
- What changed: Each panel in the lineSet grid created after the original AvgSpeed correlation plot now uses the same fixed x-axis limits; the mistaken limit on the later genotype correlation grid was removed.
- Rerun implications: No data rerun required; rerun the affected plotting cell to refresh the display.
- Validation performed: Parsed the notebook JSON and checked all notebook code cells with Python `ast` after skipping IPython magic lines.

### 2026-06-29 - QTL speed correlations by lineSet

- Slice goal: Add a lineSet-split version of the three-panel speed correlation plot in `Analyses/ShoalingQTLMappingAnalysis_2026.ipynb`.
- Passes completed: Inserted a new markdown/code cell immediately after the original speed-correlation plot.
- What changed: The notebook now plots one row per `lineSet` and one column for each original comparison: speed versus shoaling index, animal size, and thigmotaxis distance.
- Rerun implications: No data rerun required; rerun the original correlation cell and the new cell to refresh the displayed grid.
- Validation performed: Parsed the notebook JSON and checked all notebook code cells with Python `ast` after skipping IPython magic lines.

### 2026-06-29 - QTL single-genotype plot palette

- Slice goal: Remove the fake genotype color from cell 33 of `Analyses/ShoalingQTLMappingAnalysis_2026.ipynb` while preserving the F2 plot color.
- Passes completed: Replaced the two-entry palette with a single F2 palette and explicit `genotype_hue_order`.
- What changed: The point and swarm plots now both use `hue_order=['F2']` and `palette={'F2': "#1F77B4"}`.
- Rerun implications: No data rerun required; rerun cell 33 to refresh the displayed plot.
- Validation performed: Parsed the notebook JSON and smoke-tested the one-genotype seaborn point/swarm palette pattern on dummy data.

### 2026-06-26 - 2h vs 4h plot color settings

- Slice goal: Add editable plot color settings to `Analyses/ShoalingSelection_2h_vs_4h_2026.ipynb`.
- Passes completed: Inserted a plot color block at the top of the Settings cell and routed episode, genotype, reference-line, cutoff-line, baseline, and SEM-band colors through it.
- What changed: Progression plots now use named settings for episode palettes, one-hour markers, 24-episode cutoffs, zero baselines, and shaded error-band alpha values.
- Rerun implications: No data rerun required; rerun the setup/settings and plotting cells to refresh figures with edited colors.
- Validation performed: Parsed the notebook JSON, checked all code-cell syntax with IPython magic lines skipped, and scanned for remaining hard-coded plot color literals outside the new settings block.

### 2026-06-26 - Carryover plot color settings

- Slice goal: Add editable plot color settings to `Analyses/ShoalingCarryoverRawASD_2026.ipynb`.
- Passes completed: Inserted a plot color block at the top of the Settings cell and routed notebook-local line, SEM band, episode band, genotype, and reference-line colors through it.
- What changed: `draw_lineplot_with_sem` now resolves colors from split-specific palettes for episode and genotype plots, while unsplit traces and zero reference lines use named settings.
- Rerun implications: No data rerun required; rerun the setup/settings and plotting cells to refresh figures with edited colors.
- Validation performed: Parsed the notebook JSON, checked all code-cell syntax with IPython magic lines skipped, and smoke-tested the plotting helper on dummy unsplit, episode-split, and genotype-split summaries.

### 2026-06-25 - 2h aggregate progression plot

- Slice goal: Add an aggregate 2h-only shoaling-index progression plot to `Analyses/ShoalingSelection_2h_vs_4h_2026.ipynb`.
- Passes completed: Inserted a new notebook section immediately before the existing 2h by-experiment progression grid.
- What changed: Summarized `df_plot` rows with `condition_key == '2h'` by episode type and 5-minute episode number; plotted bout and linear trajectories overlaid with SEM bands; saved `attraction_progression_2026_2h.pdf`.
- Rerun implications: No pipeline rerun required; rerun the new plot cell after summaries are loaded to generate the displayed figure and PDF.
- Validation performed: Parsed the edited notebook as JSON and checked all notebook code cells with Python `ast` after skipping IPython magic lines.

### 2026-06-24 - Carryover stale-cache warnings

- Slice goal: Make stale processed carryover data obvious when cached tables are loaded after analysis settings change.
- Passes completed: Added per-experiment cache settings sidecars, loud mismatch warnings during cached loads, and passed processed-data settings from `Analyses/ShoalingCarryoverRawASD_2026.ipynb`.
- What changed: `functions/carryover_effects.py` now writes `*_settings.json` next to each processed ASD/SI cache and warns when cached settings are missing or differ from the current processing settings.
- Rerun implications: Existing caches created before this change will warn until rebuilt once with `FORCE_REPROCESS_RAW_DATA = True`; future setting changes will warn when stale cached tables are loaded.
- Validation performed: Compiled `functions/carryover_effects.py`, parsed all carryover notebook code cells, and smoke-tested matching versus changed cache settings with monkeypatched extraction.

### 2026-06-24 - Carryover per-experiment cache loading

- Slice goal: Avoid repeating raw carryover ASD/SI extraction when processed tables already exist for an experiment.
- Passes completed: Added cache-aware carryover extraction helpers and routed `Analyses/ShoalingCarryoverRawASD_2026.ipynb` through them with a `FORCE_REPROCESS_RAW_DATA` switch.
- What changed: `functions/carryover_effects.py` now writes and loads per-experiment `asd_frame` and `si_1min` caches; the notebook also saves combined cohort-level copies for manual loading.
- Rerun implications: Existing combined `asd_frame.csv.gz` alone is not enough for skipping raw processing; after one rerun, per-experiment ASD and SI cache files allow future runs to load processed data.
- Validation performed: Compiled `functions/carryover_effects.py` and parsed all carryover notebook code cells with IPython magic lines skipped.

### 2026-06-24 - Carryover notebook-local plotting

- Slice goal: Move raw-ASD carryover plotting code into `Analyses/ShoalingCarryoverRawASD_2026.ipynb` and add a 10-minute-window 1-minute SI grid.
- Passes completed: Replaced all `functions.carryover_effects` plot calls with explicit notebook plotting code, added notebook-local summary/SEM and episode-band utilities, and added the requested Analysis 2 grid grouped by episode start time window.
- What changed: Removed carryover plot functions from `functions/carryover_effects.py`; the helper now owns data extraction/preparation only.
- Rerun implications: Rerun the notebook plotting cells after `asd_frame` and `si_1min` are loaded or regenerated.
- Validation performed: Parsed the notebook JSON, checked all notebook code-cell syntax with IPython magic lines skipped, compiled `functions/carryover_effects.py`, and searched for stale `ce.plot_*` references.

### 2026-06-24 - Carryover notebook cache and progress

- Slice goal: Add visible progress reporting and temporary output caching to the raw-ASD carryover notebook.
- Passes completed: Set the notebook to the first 24 raw episode blocks, added an `INCLUDE_ESCAPEE_FISH` switch defaulting to `False`, wrote `processingSettings.csv`, `carryover_analysis_settings.json`, and `asd_frame.csv.gz` to a carryover temp-processing folder.
- What changed: Updated `Analyses/ShoalingCarryoverRawASD_2026.ipynb`; plots still consume the in-memory `asd_frame` and `si_1min` tables.
- Rerun implications: Rerun the extraction cell to refresh the cached ASD table and settings file.
- Validation performed: Parsed the notebook JSON and checked code-cell syntax with IPython magic lines skipped.

### 2026-06-24 - Raw ASD carryover notebook

- Slice goal: Create a clean notebook for frame-level ASD and 1-minute shoaling-index carryover plots.
- Passes completed: Added `Analyses/ShoalingCarryoverRawASD_2026.ipynb` and routed reusable work through `functions/carryover_effects.py`.
- What changed: Notebook loads current selection metadata, extracts raw ASD for `01k01f` and `02k20f`, plots frame-by-frame ASD over the experiment, per-episode ASD segments, genotype splits, 1-minute SI over time, and 1-minute SI averaged by episode.
- Rerun implications: Run the new notebook against accessible raw position files; no existing summary pipeline rerun is required.
- Validation performed: Parsed the notebook JSON and checked code-cell syntax with IPython magic lines skipped.

### 2026-06-23 - 2h experiment progression plot

- Slice goal: Add a per-experiment 2h shoaling-index progression plot to `Analyses/ShoalingSelection_2h_vs_4h_2026.ipynb`.
- Passes completed: Inserted a new notebook section immediately after the existing full-window progression plot.
- What changed: Summarized `df_plot` rows with `condition_key == '2h'` by experiment, episode type, and 5-minute episode number; plotted one subplot per experiment with bout and linear trajectories overlaid; saved `attraction_progression_2026_2h_by_experiment.pdf`.
- Rerun implications: No pipeline rerun required; rerun the notebook plot cells after summaries are loaded to generate the new PDF.
- Validation performed: Parsed the edited notebook as JSON and reviewed the targeted notebook diff.

### 2026-06-23 - 2h progression marker and comments

- Slice goal: Make the per-experiment 2h progression cell easier to understand and edit.
- Passes completed: Added explanatory comments throughout the plotting cell and a single editable `REFERENCE_MINUTE` setting.
- What changed: Added a red dotted vertical reference line at minute 60 to every experiment subplot.
- Rerun implications: No pipeline rerun required; rerun the notebook plot cell to refresh the displayed figure and saved PDF.
- Validation performed: Parsed the edited notebook as JSON and inspected the updated cell source.

### 2026-06-23 - Progression SD bands

- Slice goal: Use standard deviation bands instead of SEM bands for shoaling-index progression plots.
- Passes completed: Updated the full-window progression plot and the 2h per-experiment progression grid.
- What changed: Replaced `sem_si` summary columns with `sd_si=('si', 'std')` and changed shaded bands to `mean_si +/- sd_si`.
- Rerun implications: No pipeline rerun required; rerun the affected plot cells to refresh displayed outputs and saved PDFs.
- Validation performed: Parsed the edited notebook as JSON and checked executable source for remaining `sem_si` references.

### 2026-06-23 - Revert progression bands to SEM

- Slice goal: Restore standard-error bands for shoaling-index progression plots.
- Passes completed: Updated the full-window progression plot and the 2h per-experiment progression grid.
- What changed: Replaced `sd_si=('si', 'std')` with `sem_si=('si', sem)` and changed shaded bands back to `mean_si +/- sem_si`.
- Rerun implications: No pipeline rerun required; rerun the affected plot cells to refresh displayed outputs and saved PDFs.
- Validation performed: Parsed the edited notebook as JSON and checked the progression source for `sem_si` aggregation and band references.

### 2026-06-19 - Active notebook path routing

- Slice goal: Align notebook workflow routing with the current `Analyses/` notebook layout.
- Passes completed: Updated notebook router, notebook stage map, and current-state notes from stale `exampleAnalysis/` references to current `Analyses/` and `DeprecatedAnalyses/LarschAndBaier2018/` paths.
- What changed: Documentation-only route corrections for active selection, history, QTL, size, and historical figure notebooks.
- Rerun implications: No analysis rerun required.
- Validation performed: Checked notebook file locations and searched docs for remaining stale path references.

### 2026-06-19 - Selection notebook heading structure

- Slice goal: Add informative hierarchical markdown titles to the current selection and selection-history example notebooks.
- Passes completed: Inserted and refined `#`, `##`, and `###` headings in `ShoalingSelectionAnalysis_2025_slim_clean.ipynb` and `ShoalingSelectionAnalysis_2025History.ipynb`.
- What changed: Organized setup, shoaling-index analyses, metric checks, filtering, escapee analysis, selection grid, and history/cohort sections without changing notebook code cells.
- Rerun implications: Markdown-only change; no analysis rerun required.
- Validation performed: Parsed all three relevant notebooks and printed heading outlines; confirmed code-cell counts stayed stable for the edited notebooks.

### 2026-06-19 - Shared notebook loading headers

- Slice goal: Mirror the early loading/settings markdown headers from the selection-history notebook into the slim selection and QTL notebooks.
- Passes completed: Added matching headers for metadata loading, processing settings, processed summaries, episode-level summaries, and statistic helpers.
- What changed: Updated `Analyses/ShoalingSelectionAnalysis_2025_slim_clean.ipynb` and `Analyses/ShoalingQTLMappingAnalysis_2026.ipynb` without changing notebook code cells.
- Rerun implications: Markdown-only change; no analysis rerun required.
- Validation performed: Parsed the three relevant notebooks and checked early heading outlines and code-cell counts.

### 2026-06-22 - 2h vs 4h single-pass processing

- Slice goal: Avoid running the long processing stage twice in `Analyses/ShoalingSelection_2h_vs_4h_2026.ipynb`.
- Passes completed: Changed the notebook to write one full-experiment processing settings CSV, run `experiment_set` only for `4h_all`, load the full summaries once, and derive the 2h window from `episode_number <= 24`.
- What changed: Removed condition-specific processing tables and downstream duplicated summary loading while preserving the existing 2h vs 4h/all plotting interface.
- Rerun implications: Full summaries may need one rerun in the `4h_all` processing folder; the 2h window is now an in-memory subset and does not need its own processing output.
- Validation performed: Parsed the edited notebook as JSON, searched for stale condition-loop references, and compiled all 10 transformed notebook code cells with the `jlsocial` Python environment.

## Template

### YYYY-MM-DD - Short label

- Slice goal:
- Passes completed:
- What changed:
- Rerun implications:
- Validation performed:
