# Social Behavior Stage Map

Purpose: navigate the ordered analysis flow from experiment definitions to social behavior outputs.

Use this file for questions about stage order, writer ownership, reruns, or downstream impact.

## End-to-end stages

1. Experiment list setup
   - Entry: notebook-generated CSV or user-selected CSV.
   - Owner: `models/experiment_set.py`.
   - Key behavior: reads rows, applies `MissingOnly`, instantiates `experiment(row)`.

2. Experiment metadata and raw load
   - Owner: `models/experiment.py`, `ExperimentMeta`, `experiment.loadData`.
   - Inputs: `txtPath`, `aviPath`, `pairList`, `epiDur`, `episodes`, `ProcessingDir`, `outputDir`, ROI/scale settings.
   - Handles old Bonsai, VR tracking, idTracker-like `.npy`/CSV cases.

3. Calibration and size caches
   - Owners: `models/experiment.py`, `functions/video_functions.py`, `functions/getAnimalSizeFromVideo.py`.
   - Outputs: `*_anSize.csv`, `anSizeAll.csv` where produced by helpers.

4. Animal and pair linking
   - Owners: `models/animal.py`, `models/pair.py`, `models/AnimalTimeSeriesCollection.py`.
   - Concepts: animal identity, pair episodes, shifted controls, speed, position, inter-animal distance.

5. Episode statistics
   - Owner: `models/experiment.py`.
   - Outputs: `*_siSummary_epi<episodeDur>.csv`.
   - Columns include animal/set identifiers, partner, `si`, episode fields, speed, size, thigmotaxis, bouts, leadership, sync fields.

6. Neighborhood maps
   - Owners: `models/experiment.py`, `models/AnimalTimeSeriesCollection.py`.
   - Output: `*MapData.npy`.
   - Shape convention in writer: episode-pair rows by measure by data/shuffle by map grid.

7. Notebook aggregation and figures
   - Owners: notebooks for orchestration, `functions/notebookHelper.py` and plotting helpers for reusable work.
   - Downstream consumers should not redefine writer-stage output semantics.

## Navigation notes

- Use `canonical-outputs.md` before changing filenames or columns.
- Use `symbol-index.md` to find the narrowest class/function owner.
- Open notebooks only after checking whether the writer module owns the behavior.
