# Recent Changes - Social Behavior Analysis

Append meaningful completed changes here.

### 2026-07-06 - Neighborhood map histogram compatibility

- Slice goal: Fix neighborhood-map generation under current NumPy for the optional `SaveNeighborhoodMaps` processing path.
- Passes completed: Updated the neighborhood-density writer methods used by `experiment.saveExpData()` without changing notebook orchestration or `MapData.npy` axes.
- What changed: Replaced removed `np.histogramdd(..., normed=True)` usage in `models/AnimalTimeSeriesCollection.py` with `density=True` and derived the normalization scale from `mapBins`.
- Rerun implications: Rerun the neighborhood-map notebook processing cell for missing map outputs; existing valid `MapData.npy` files do not need migration.
- Validation performed: Direct smoke check for `neighborMat()` and `neighborMat_filt()` against `np.histogramdd(..., density=True)` expected output.

### 2026-06-24 - Carryover extraction controls

- Slice goal: Make raw carryover extraction easier to monitor and constrain it to the planned analysis subset.
- Passes completed: Added per-experiment progress reporting, first-24-chronological-episode limiting before episode-label filtering, and an `include_escapees` switch that excludes `esc*` genotypes by default.
- What changed: Updated `functions/carryover_effects.py`; no canonical 5-minute summary writer behavior changed.
- Rerun implications: Rerun `Analyses/ShoalingCarryoverRawASD_2026.ipynb` to regenerate the carryover ASD/SI tables with escapees excluded.
- Validation performed: Compiled and imported `functions/carryover_effects.py`.

### 2026-06-24 - Raw ASD carryover helpers

- Slice goal: Add reusable helpers for raw animal-stimulus distance and 1-minute attraction carryover analyses without changing the canonical 5-minute shoaling writer.
- Passes completed: Inspected `models/experiment.py`, `models/pair.py`, and `models/AnimalTimeSeriesCollection.py` for raw trajectory, stimulus, episode, and shifted-control semantics.
- What changed: Added `functions/carryover_effects.py` with direct raw position loading, frame-level ASD extraction, 1-minute shoaling-index computation using within-episode stimulus time shifts of at least 30 seconds, and plotting helpers.
- Rerun implications: Existing `*_siSummary_epi5.0.csv` outputs are unchanged; rerun only the new notebook to generate raw-ASD and 1-minute SI views.
- Validation performed: Compiled `functions/carryover_effects.py`.

### 2026-06-19 - Selection-shoaling pipeline memory

- Slice goal: Capture stable agent memory for the current selection-shoaling metadata-to-summary pipeline.
- Passes completed: Read the required routers and references, inspected `Analyses/ShoalingSelectionAnalysis_2025_slim_clean.ipynb`, and checked owning model/helper modules for episode, pair, summary, and shoaling-index behavior.
- What changed: Added a documentation-only pipeline memory block to `social-behavior-stage-map.md` and a repo rule requiring grounded claims and explicit permission before analysis-code changes during pipeline-understanding tasks.
- Rerun implications: No analysis rerun required.
- Validation performed: Static inspection of notebook cells and owner modules; no code execution against raw data.

## Template

### YYYY-MM-DD - Short label

- Slice goal:
- Passes completed:
- What changed:
- Rerun implications:
- Validation performed:
