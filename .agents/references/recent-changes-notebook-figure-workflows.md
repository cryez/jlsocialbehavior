# Recent Changes - Notebook Figure Workflows

Append meaningful completed changes here.

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
