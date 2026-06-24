# Recent Changes - Notebook Figure Workflows

Append meaningful completed changes here.

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
