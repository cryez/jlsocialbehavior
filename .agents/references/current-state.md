# Current State

Purpose: collect practical caveats and mixed-authority notes for future agents.

Use this file when repo authority is unclear or a task touches legacy/migration boundaries.

## Repo shape

- This is a Python 3.6-era scientific analysis repository with notebooks, reusable modules, wrappers, GUI tools, and historical paper reproduction assets.
- `readme.md` describes the historical Larsch and Baier 2018 analysis workflow and raw data source.
- Current active analysis notebooks also live under `exampleAnalysis/`.
- `.agents/` now provides routing and handoff docs; `coding.md` is the baseline coding behavior file.

## Authority notes

- `models/` and `functions/` are the authoritative reusable code layers.
- `LarschAndBaier2018/` notebooks are historical workflow surfaces and should be changed carefully.
- `exampleAnalysis/` notebooks are current analysis surfaces but should still avoid accumulating reusable logic.
- `playground/` and `obsolete/` contain experimental or legacy code; do not use them as authority unless directly targeted.
- Directories such as `Lib/`, `DLLs/`, `conda-meta/`, `Tools/`, and `Library/` look like local environment artifacts, not project source.

## Practical caveats

- Some code uses Python 2/early Python 3-era styles and old library conventions.
- Many validations may require local raw data, ffmpeg, OpenCV, GUI support, or notebook execution.
- If full validation is unavailable, run the smallest import/static/contract check possible and record what could not be verified.

## Working tree note

- Preserve unrelated user changes. At setup time the worktree already had a deleted root `Copilot_FFMPEG_SETUP.md` and untracked `documentation_cr/`.
