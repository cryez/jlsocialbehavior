# Symbol Index

Purpose: compact ownership index for public or workflow-called symbols.

Use this file when choosing the narrowest code owner before editing.

## Trusted implementation patterns

- `models/` owns experiment, animal, pair, time-series, and shape-analysis semantics.
- `functions/` owns reusable helpers for notebooks, plotting, image/video processing, statistics, and vector fields.
- Top-level scripts and GUIs own orchestration, command construction, and user interaction.
- Notebooks own parameter setup, stage order, and display/composition only.

## Models

- `models.experiment_set.experiment_set`: batch wrapper over experiment-definition CSV rows; owns `MissingOnly` and per-row experiment instantiation.
- `models.experiment.ExperimentMeta`: experiment metadata, file paths, defaults, ROI/scale discovery, and output directories.
- `models.experiment.experiment`: raw trajectory loading, animal/pair linking, summary/map/size output writing, overview plotting.
- `models.pair.Pair`: pair-level behavior such as inter-animal distance, shifted controls, and shoaling index.
- `models.animal.Animal`: animal-level wrapper around trajectories and derived time series.
- `models.AnimalTimeSeriesCollection.AnimalTimeSeriesCollection`: position, speed, curvature, thigmotaxis, neighborhood maps, force maps.
- `models.AnimalBoutSeriesCollection.AnimalBoutSeriesCollection`: bout-series semantics.
- `models.geometry`: `Trajectory`, `Circle`, `Region`, `Vector`, angle and distance geometry helpers.
- `models.AnimalShapeParameters.get_AnimalShapeParameters`: shape/tail/body extraction entrypoint.
- `models.AnimalShapeParameters_MP.get_AnimalShapeParameters`: multiprocessing variant of shape extraction.

## Functions

- `functions.notebookHelper.readExperiment`: notebook-facing experiment loading helper.
- `functions.notebookHelper.savedCsvToDf`: aggregation of saved summary CSVs.
- `functions.notebookHelper.computeExpTimeOfDay`, `cohend`, `groupCohen`, `groupPower`: notebook statistics/time helpers.
- `functions.video_functions.get_pixel_scaling`: video/ROI-derived scale owner.
- `functions.video_functions.extract_frames_ffmpeg`: ffmpeg frame extraction owner.
- `functions.video_functions.getAnimalLength`, `getAnimalSize`: animal size from frame/video owner.
- `functions.getAnimalSizeFromVideo.getAnimalSizeFromVideo`: video-backed animal-size extraction.
- `functions.getMedVideo.getMedVideo`: median/background video generation.
- `functions.getVideoProperties.getVideoProperties`: video metadata lookup.
- `functions.gui_circle.get_circle_rois`: interactive ROI definition.
- `functions.ImageProcessor`: reusable image segmentation, contour, skeleton, morphology, and crop helpers.
- `functions.plotFunctions_joh`: reusable plot helpers for maps and group comparisons.
- `functions.paperFigureProps.paper`: global paper-style plotting defaults.
- `functions.vector_field_analysis.VectorFieldAnalysis`: vector-field analysis orchestration.
- `functions.vector_field_analysis.calc_*`, `plot_*`: vector-field statistics and plots.
- `functions.matrixUtilities_joh`: geometry/path/math utility helpers used across modules.

## Scripts and wrappers

- `main.py`: simple batch/single-experiment entrypoint.
- `reRunSizeAnalysis.py`: size rerun wrapper.
- `ffmpegSplit4_module_bgDiv.py`: ffmpeg split/background-division wrapper.
- `processingVideo.py`, `rotationWrapper.py`: video preprocessing orchestration.
- `vidGui.py`, `VidGui2ArenaShoal.py`: GUI entrypoints.
- `scripts/pairLists.py`, `scripts/calibration.py`, `scripts/splitMultiPairTxt.py`: operational helper scripts.
