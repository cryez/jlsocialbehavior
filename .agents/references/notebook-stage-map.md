# Notebook Stage Map

Purpose: route notebook and figure work without reading entire notebooks first.

Use this file for tasks involving `Analyses/*.ipynb`, `DeprecatedAnalyses/LarschAndBaier2018/*.ipynb`, figure composition, or notebook-specific reruns.

## Workflow groups

1. Historical paper reproduction
   - Entry: `DeprecatedAnalyses/LarschAndBaier2018/2018_00_GenerateAllFigures.ipynb`.
   - Related notebooks: `2018_BM_*` and `composeFigure*.ipynb`.
   - Purpose: load analysis outputs, run panel-specific statistics/plots, compose final figures.

2. Current example analyses
   - Entries: `Analyses/ShoalingSelectionAnalysis_2025_slim_clean.ipynb`, `Analyses/ShoalingSelectionAnalysis_2025History.ipynb`, `Analyses/ShoalingSelection_2h_vs_4h_2026.ipynb`, `Analyses/ShoalingNeighborhoodMaps_2026.ipynb`, `Analyses/ShoalingTrajectoryGrid_2026.ipynb`, `Analyses/ShoalingCarryoverRawASD_2026.ipynb`, `Analyses/ShoalingQTLMappingAnalysis_2026.ipynb`, and `Analyses/size_data_analysis.ipynb`.
   - Purpose: selection-shoaling analysis, current data exploration, neighborhood-map summaries, raw ASD/carryover checks, QTL/cFos examples, size summaries.

3. Helper-backed notebook work
   - Owners: `functions/notebookHelper.py`, `functions/carryover_effects.py`, `functions/plotFunctions_joh.py`, `functions/paperFigureProps.py`, `functions/vector_field_analysis.py`.
   - Use helpers for repeated loading, statistics, vector fields, and plotting idioms.

## Key outputs

- Figure files in configured `output` locations.
- Saved plots from `functions/vector_field_analysis.py`, including vector-field and attraction/thigmotaxis images.
- Downstream tables loaded from `*_siSummary_epi*.csv`, `*MapData.npy`, and size files.

## Navigation notes

- Read `canonical-outputs.md` before changing notebook assumptions about generated file names or columns.
- If a notebook contains reusable transformations, move them to the owning module only when the task requires a refactor.
- For plot changes, render or inspect the resulting artifact before claiming success.
