# Recent Changes - Notebook Figure Workflows

### 2026-07-24 - Sel1 versus Sel3 hi/lo loom-response plots

- Slice goal: Compare hi and lo loom responses separately within Sel1 and Sel3 line families while excluding Sel1_GC.
- What changed: Appended family-specific legacy center-distance, merged-response, maximum-velocity time/fit, and both side-layout plots to `Analyses/LoomAnalysisCR.ipynb`; Sel1/TLSel1 and Sel3/TLSel3 reuse the existing experiment-level caches with shared plot scales.
- Rerun implications: No cache rebuild is required; rerun the notebook through the new final section after the compact loom tables have loaded.
- Validation performed: Notebook JSON, executable-cell syntax, line-family classification, genotype filtering, and synthetic plot rendering were checked.

### 2026-07-24 - Loom cohort date filtering

- Slice goal: Replace the fixed year selector in `Analyses/LoomAnalysisCR.ipynb` with editable date-based cohort selection.
- What changed: Added inclusive start-date and exclusion-range modes, removed the fixed expected-experiment-count warning, and report the number of selected experiments after metadata/date filtering.
- Rerun implications: Rerun the notebook from its settings and metadata-selection cells after changing the date mode or date values; matching per-experiment loom caches remain reusable.
- Validation performed: Added helper tests for inclusive boundaries, missing dates, and invalid date settings; notebook JSON and executable-cell syntax checks will be run after the edit.

### 2026-07-22 - Gaussian peak fits for max velocity over time

- Slice goal: Capture the initial max-velocity rise at loom sizes 1 and 5 before comparing the subsequent genotype-specific decline.
- What changed: Replaced the estimated-floor exponential curves in `Analyses/LoomAnalysisCR.ipynb` with bounded estimated-floor Gaussian peak fits, expanded the time axis to include the complete protocol, and report peak timing plus the maximum post-peak velocity-loss rate and related width/half-decay summaries.
- Rerun implications: No raw-data or cache rebuild is required; rerun the time-versus-maximum-velocity plot cell after loading `trial_max_velocity`.
- Validation performed: Parsed and syntax-checked the notebook, recovered known Gaussian parameters in split and pooled synthetic tests, checked fit failure modes and derived-rate formulas, and smoke-rendered the eight cached experiments for visual inspection.

### 2026-07-22 - Genotype-specific velocity decay curves

- Slice goal: Compare how quickly post-loom maximum velocity decreases over experiment time for each displayed genotype.
- What changed: Replaced the pooled Pearson annotation in `Analyses/LoomAnalysisCR.ipynb` with independent nonnegative estimated-floor exponential fits, genotype-coloured curve overlays, decay constants in the legend, and a descriptive table of floors, amplitudes, initial decrease rates, half-lives, fit quality, and point counts.
- Rerun implications: No raw-data or cache rebuild is required; rerun the time-versus-maximum-velocity plot cell after loading `trial_max_velocity`.
- Validation performed: Parsed and syntax-checked the notebook, smoke-rendered split and pooled modes with synthetic exponential data, checked failure handling, and visually inspected the split plot.

### 2026-07-22 - Loom-size shapes in maximum-velocity side plots

- Slice goal: Make loom maximum size shape-coded in both maximum-velocity-by-side figures while retaining genotype colour coding.
- What changed: Added deterministic `SIZE_MARKERS`, removed loom-size colour encoding, applied size markers to individual points, and split the legends into genotype-colour and loom-size-shape entries. Pooled mode uses neutral box/point colours.
- Validation performed: Parsed the notebook and smoke-rendered both side plots in split and pooled modes; visually inspected the split figure for consistent genotype colours, size shapes, and readable legends.

### 2026-07-22 - Genotype-aware loom-response plots

- Slice goal: Compare user-selected fish genotypes throughout the multi-experiment loom notebook while preserving pooled views.
- What changed: Added normalized `AllAn` genotype mapping, pooled plus per-genotype loom cache rows, dynamic genotype catalog/selection controls defaulting to hi/lo/F2, genotype-aware versions of all seven existing figure outputs, and descriptive maximum-speed and legacy-response summaries with experiment and fish counts. The cache schema is now version 2, so old pooled-only caches reprocess automatically.
- Rerun implications: Rerun `Analyses/LoomAnalysisCR.ipynb` from metadata selection through processing; the first run rebuilds the four per-experiment loom caches, while later plot-switch changes reuse them.
- Validation performed: Compiled the helper, parsed every notebook code cell, passed targeted metadata/extraction/cache-contract tests, and smoke-rendered all plot cells with synthetic pooled and three-genotype data in split and pooled modes. Live metadata and raw-data rendering were unavailable because the network share denied access in the agent environment.

Append meaningful completed changes here.

### 2026-07-21 - Detail SI slowdown cluster bootstrap

- Slice goal: Make every sampling, filtering, and inferential step of the SI slowdown bootstrap auditable from the notebook and helper source.
- What changed: Added a step-by-step description of per-stimulus whole-experiment resampling, duplicate-cluster relabeling, retained fish/time dependence, model refitting and genotype reweighting, failed and nonpositive draw handling, requested-draw rate denominators, the positive-total-increase gate, the conditional crossing-time interval, and the maximum-deviation simultaneous upper band. Clarified that the default performs 500 refits per stimulus rather than one paired set of 500 two-stimulus refits, and documented cluster-count and late-window interpretation limits.
- Rerun implications: Documentation/comments only; no processing, bootstrap, table, or figure rerun is required.
- Validation performed: Parsed the notebook JSON and checked the expanded bootstrap source against `functions/si_slowdown.py`; targeted contracts verified the sampling unit, duplicate relabeling, draw accounting, positive-increase gate, conditional interval, simultaneous-band formula, and per-stimulus refit count. Python execution remained unavailable because no working interpreter is installed in the checkout or on PATH.

### 2026-07-21 - Move 2h SI slowdown inference after progression-by-experiment

- Slice goal: Keep the 2h SI slowdown inference at the end of the 2h progression sections.
- What changed: Moved the slowdown explanation, fit, and plot cells together to immediately follow the 2h progression-by-experiment grid; no analysis code or outputs changed.
- Rerun implications: No processing rerun is required; rerun the moved slowdown cells only if refreshed inference tables or figures are needed.
- Validation performed: Confirmed notebook cell ordering and preserved slowdown cell contents, parsed/syntax-checked the notebook, and ran the SI slowdown unittest suite.

### 2026-07-21 - Explain SI slowdown inference and vertical markers

- Slice goal: Make the SI slowdown estimand, uncertainty criterion, outputs, and figure markers understandable from the notebook and helper source.
- What changed: Expanded the notebook markdown with the forward-increment equation, persistence rule, mixed-model hierarchy, experiment-cluster bootstrap, simultaneous upper-band interpretation, result/diagnostic guidance, and an explicit explanation of the solid cyan 100-minute line. Documented every slowdown setting and the analysis/plot cells, expanded `functions/si_slowdown.py` docstrings and intent comments, added dashed/solid vertical-line legend keys, and clarified that lower-panel x-values start forward same-stimulus intervals.
- Rerun implications: No processing or inference rerun is needed for the documentation changes. Rerun only the slowdown plot cell after the existing slowdown tables are in memory to refresh the saved PDF with the new legend keys and x-axis wording.
- Validation performed: Parsed the notebook JSON, inspected the three slowdown cell sources, and checked targeted documentation/plot-label contracts. No runnable Python interpreter was available in this checkout or on PATH, so Python compilation and rendered figure inspection were unavailable.

### 2026-07-21 - Restrict SI slowdown inference to the 2h window

- Slice goal: Run SI slowdown-point inference only on the first 24 five-minute episodes and remove stale full-window slowdown artifacts.
- What changed: Moved the slowdown analysis under the 2h progression summary, restricted its raw input to `episode_number <= 24`, renamed notebook outputs with the `_2h` suffix, and deleted the seven stale `_4h_all` CSV/PDF artifacts from the configured output directory.
- Rerun implications: Rerun the slowdown cells after loading the summaries to regenerate the seven `_2h` outputs; the full-window progression plot remains unchanged.
- Validation performed: Notebook JSON parsed; cell order, episode-limit assertion, input source, and output-name contracts passed; all seven stale external artifacts were verified absent after deletion. Python compilation and unit tests were unavailable because the installed Python command is a nonfunctional Windows Store alias.

### 2026-07-21 - Switchable SEM and confidence-interval plot uncertainty

- Slice goal: Allow `Analyses/ShoalingSelection_2h_vs_4h_2026.ipynb` plots to show 95% confidence intervals instead of SEM while preserving the current default.
- What changed: Added the editable `PLOT_CONFIDENCE_INTERVALS` setting, retained parallel SEM and 95% CI summary columns, and routed progression, normalized-SI, per-experiment, and slowdown uncertainty displays through the selected column.
- Rerun implications: No processing rerun is required; rerun the settings and affected summary/plot cells after changing the setting.
- Validation performed: Parsed the notebook JSON and passed source-contract checks for both uncertainty modes, including singleton guards and selector coverage; Python AST compilation and rendered smoke tests were unavailable because no working project Python interpreter is present in this session.

### 2026-07-21 - Shoaling-index slowdown inference

- Slice goal: Estimate when each stimulus-specific SI increase becomes smaller than an editable fraction of the total fitted experiment increase.
- What changed: Added `functions/si_slowdown.py` with spline mixed models, experiment-clustered bootstrap inference, persistent crossings, simultaneous one-sided upper bounds, genotype standardization, residual/coverage checks, spline and leave-one-experiment-out sensitivity tables, and an asymptotic mixed-model comparison. Extended `Analyses/ShoalingSelection_2h_vs_4h_2026.ipynb` with editable settings, result exports, and fitted-SI/fraction plots while preserving the canonical summary writer and existing progression plot.
- Rerun implications: No SI processing rerun is required. Rerun the notebook from its imports/settings and loaded-summary cells; the default requests 500 mixed-model bootstrap refits per stimulus (1,000 primary bootstrap refits across two stimuli) and therefore takes materially longer than a descriptive plot cell.
- Validation performed: Compiled the helper and tests, parsed and syntax-checked every notebook code cell, ran three unit tests, and smoke-tested both stimulus-specific clustered bootstraps plus the profiled asymptotic and leave-one-experiment-out paths on synthetic repeated-measures data.

### 2026-07-20 - Mortality bars by line or lineage

- Slice goal: Show how selection lines or editable ancestry lineages contribute to both mortality record histograms and tank-normalized mortality proportions without changing either plot's statistic.
- What changed: Added a shared `MORTALITY_COLOR_BY` setting to `temp/fish_analyzes.ipynb`; `none` preserves the three original category colours, while `line` and `lineage` draw additive stacks and expose record-count and mean-proportion contribution tables. Lineage mode warns and excludes unmapped records and tanks before calculating bins and denominators; `MORTALITY_LINE_FILTER` remains limited to the tank-normalized section.
- Rerun implications: Rerun the settings and both mortality sections after changing the colour mode, lineage mapping, age-bin width, mortality line filter, or source workbook.
- Validation performed: Parsed and compiled all 12 code cells; ran all six plots in all three modes against the real workbook; confirmed `none` and `line` retain 320 records/284 usable tanks, lineage mode warns once per section and retains 311 records/273 tanks after excluding four unmapped lines, all record stacks equal histogram counts, all normalized stacks equal the original means, category colours and legends are correct, one- and two-month bins work, single/multiple line filters work, duplicate mapping validation is lineage-only, invalid modes fail, and representative plots in every mode are readable.

### 2026-07-20 - Uncoloured incross-failure age mode

- Slice goal: Provide a pooled, neutral version of the incross-failure-by-age plot alongside lineage- and line-coloured views.
- What changed: `temp/fish_analyzes.ipynb` now accepts `INCROSS_FAILURE_COLOR_BY = \"none\"`, which includes all eligible selection lines, draws one gray failure-proportion bar per populated age class, and suppresses the grouping legend without consulting `LINEAGE_GROUPS`.
- Rerun implications: Rerun the settings, crossing-history, and age-bin cells after changing `INCROSS_FAILURE_COLOR_BY`.
- Validation performed: Parsed and compiled all 12 code cells; ran all three modes against the real workbooks; confirmed `none` retains 126 crosses/27 failures with one gray series, exact failure-proportion heights, no lineage warnings, and no legend; reconfirmed lineage mode excludes the current unmapped cross with one warning, line mode retains all crosses, invalid values fail clearly, and visually inspected the uncoloured render.

### 2026-07-20 - Optional lineage exclusions for incross failures

- Slice goal: Allow users to omit selection lines from the editable ancestry mapping without blocking the lineage-coloured age analysis.
- What changed: Lineage mode in `temp/fish_analyzes.ipynb` now warns once about unmapped lines and excludes their crosses before calculating age-bin totals, failure proportions, stacks, and sample-size labels; line mode remains independent of the lineage mapping.
- Rerun implications: Rerun the settings, crossing-history, and age-bin cells after adding or removing lines from `LINEAGE_GROUPS`.
- Validation performed: Parsed and compiled all 12 code cells; ran complete and user-edited mappings against the real workbooks; confirmed the complete result remains 126 crosses/27 failures, omitting `TL sel1 lo9xTLN inx` warns once and leaves 125 lineage-mode crosses with updated denominators, line mode retains all 126 crosses without warning, stacks match failure proportions, and multiple omissions, duplicate assignments, invalid modes, and an all-unmapped cohort behave as intended; visually inspected the partial-lineage render.

### 2026-07-20 - Switchable lineage coloring for incross failures

- Slice goal: Let the fish-age incross-failure stacks be grouped and coloured by editable ancestry lineages while retaining the original per-line view.
- What changed: Added a top-level `INCROSS_FAILURE_COLOR_BY` switch and editable nine-lineage mapping to `temp/fish_analyzes.ipynb`; the age-bin failure cell now validates lineage assignments and summarizes, colours, and labels stacks by either lineage or selection line without changing denominators.
- Rerun implications: Rerun the settings, crossing-history, and age-bin cells after changing the display switch, lineage mapping, filters, bin width, or source workbook.
- Validation performed: Parsed and compiled all 12 code cells; ran both lineage and line modes against the real workbooks; confirmed 126 eligible crosses, 27 failures, unchanged stacks across 12 one-month bins, the original 11 line segments, six represented lineage segments, correct legends, readable rendered plots, six two-month bins, and clear rejection of invalid switches and missing or duplicate lineage assignments.

### 2026-07-20 - Tank-normalized mortality proportions by age

- Slice goal: Compare the proportion of each tank's initial fish dying within age classes, with an editable selection-line filter.
- What changed: Extended `temp/fish_analyzes.ipynb` with `Plate`-normalized, non-cumulative mortality summaries and three plots for combined qualifying mortality, overall-bad-shape sacrifices, and found-dead events; only those two causes are included, tanks are equally weighted, and the setting accepts `all`, one line, or multiple lines.
- Rerun implications: Rerun the loading/settings, mortality, and new mortality-proportion cells after changing `MORTALITY_LINE_FILTER`, `AGE_BIN_MONTHS`, or `fish_database.xlsx`.
- Validation performed: Parsed and compiled all 12 code cells; ran the new section against the real workbook; confirmed 37 valid lines, 284 usable tanks, 1,059 found-dead fish, 184 bad-shape fish, exclusion of 2,044 old-age/no-use fish, bounded/additive proportions, three rendered plots, single/multiple/case-insensitive/zero-death filters, two-month bins, and rejection of invalid filters, widths, tank metadata, and mortality amounts.

### 2026-07-19 - Cumulative near-maximum SI probability progression

- Slice goal: Show the cumulative probability that pooled fish have reached at least 95% of their own stimulus-specific maximum SI during the first 2 hours.
- What changed: Added persistent per-fish/type reached states and a pooled continuous-versus-bout-like cumulative probability trajectory with observed-fish SEM and counts, bounded probability bands, and a dedicated PDF output to `Analyses/ShoalingSelection_2h_vs_4h_2026.ipynb`; fish with missing SI are omitted only from the current episode's denominator.
- Rerun implications: No processing rerun is required; rerun the maximum-normalized calculation and new probability cells to create `si_near_max_probability_progression_2026_2h.pdf`.
- Validation performed: Parsed and syntax-checked every notebook code cell, then smoke-tested exact-threshold inclusion, persistent reached states after SI declines and across missing episodes, independent stimulus histories, category-specific exclusions, observed-only denominators, pooled probabilities/SEM/counts, first-episode inclusion, bounded bands, plot labels, axis limits, legend, and PDF target with synthetic data.

### 2026-07-19 - Skip recordings without loom episodes

- Slice goal: Let multi-experiment loom analysis continue past recordings that do not contain supported `CLfull###L/R` stimulus episodes.
- What changed: Loom collection now warns once per skipped experiment, writes no cache for it, preserves valid experiments, and raises a clear final error when every experiment is skipped.
- Rerun implications: Rerun the loom data-collection cell; existing valid caches remain compatible.
- Validation performed: Compiled the helper and smoke-tested mixed, all-invalid, valid cached, no-cache-on-skip, and unrelated-error behavior with synthetic data.

### 2026-07-19 - Maximum-normalized SI progression

- Slice goal: Replace episode-to-episode SI changes with SI levels expressed relative to each fish's own stimulus-specific maximum.
- Passes completed: Simplified the final section of `Analyses/ShoalingSelection_2h_vs_4h_2026.ipynb` to pool normalized fish observations directly for the cohort plot and within experiments for the grid.
- What changed: Differencing and the pooling-mode switch were removed; first episodes are included, category-specific invalid-SI exclusion remains active, SEM is calculated across fish, and two newly named normalized-progression PDFs replace the old increase outputs in notebook code.
- Rerun implications: No processing rerun is required; rerun the normalized calculation and plotting cells to create `si_normalized_progression_2026_2h.pdf` and `si_normalized_progression_2026_2h_by_experiment.pdf`. Previously generated increase PDFs are not deleted.
- Validation performed: Parsed and compiled all notebook cells and smoke-tested per-fish 100% maxima, category-specific exclusions, retained negative normalized observations, first-episode inclusion, pooled means and SEM, nine experiment panels, labels, and new PDF targets with synthetic data.

### 2026-07-19 - Category-specific invalid-SI exclusion

- Slice goal: Allow SI-increase plots to run when individual fish have no positive SI maximum for one or both stimulus categories.
- Passes completed: Replaced the fatal maximum-SI validation in `Analyses/ShoalingSelection_2h_vs_4h_2026.ipynb` with an auditable fish/type exclusion table and category-specific filtering.
- What changed: Fish/type combinations with nonfinite or nonpositive maximum SI are reported and removed before normalization; a fish remains eligible in its other stimulus category when that maximum is valid.
- Rerun implications: No processing rerun is required; rerun the SI-increase calculation and plot cells to regenerate the existing PDFs.
- Validation performed: Parsed and compiled the notebook and smoke-tested one-category exclusion, two-category exclusion, retained valid maxima, both pooling modes, pooled sample counts, and aggregate/grid rendering with synthetic data.

### 2026-07-19 - Fish-pooled SI increase modes

- Slice goal: Match the SI progression hierarchy by pooling fish in the episode-to-episode SI increase plots while retaining an alternate pooled-means calculation.
- Passes completed: Revised `Analyses/ShoalingSelection_2h_vs_4h_2026.ipynb` with a `SI_INCREASE_POOLING_MODE` switch, per-fish/per-stimulus maxima, pooled fish-change summaries, and pooled-normalized-mean summaries.
- What changed: The default `fish_changes` mode pools normalized fish-level changes and shows SEM across fish; `pooled_means` differences pooled normalized SI and omits uncertainty bands. Experiment-balanced aggregation and experiment/type denominators were removed from this analysis.
- Rerun implications: No processing rerun is required; rerun the revised episode-to-episode cells after `df_plot` is loaded to overwrite the existing PDFs.
- Validation performed: Parsed and compiled all notebook cells and smoke-tested unequal experiment sizes, distinct fish/type maxima, pooled weighting, both switch modes, SEM-band behavior, invalid settings and maxima, first-occurrence omission, time alignment, nine panels, labels, and PDF targets with synthetic data.

### 2026-07-18 - Stimulus-specific SI maximum normalization

- Slice goal: Express episode-to-episode SI changes relative to the maximum SI reached separately for continuous and bout-like stimuli within each experiment.
- Passes completed: Revised the episode-to-episode section of `Analyses/ShoalingSelection_2h_vs_4h_2026.ipynb` to derive experiment/type maxima from animal-averaged episode SI and use them as distinct denominators.
- What changed: Each animal-level same-type SI difference is now reported as a percentage of its experiment and stimulus type's maximum mean SI; the overall and experiment-grid plots retain their existing aggregation and output filenames.
- Rerun implications: No processing rerun is required; rerun the revised episode-to-episode cells after `df_plot` is loaded to overwrite the two PDFs.
- Validation performed: Parsed and compiled the notebook and smoke-tested type-specific denominators, normalized changes, invalid-maximum rejection, unequal experiment sizes, equal experiment weighting, time alignment, labels, nine panels, and PDF targets with synthetic data.

### 2026-07-17 - Episode-to-episode SI increase plots

- Slice goal: Show how SI changes between successive same-type 5-minute episodes during the first 2 hours, both across the cohort and within each experiment.
- Passes completed: Extended `Analyses/ShoalingSelection_2h_vs_4h_2026.ipynb` with animal-level percentage-point changes, equal-experiment aggregation, an overall plot, and a nine-panel experiment grid.
- What changed: Continuous (`01k01f`) and bout-like (`02k20f`) changes are aligned to the current episode start, with the first occurrence of each type omitted; bands show SEM across experiments in the overall plot and across animals in each experiment panel.
- Rerun implications: No processing rerun is required; rerun the new cells after `df_plot` is loaded to create the two new PDFs in the existing output directory.
- Validation performed: Parsed the notebook JSON, compiled all 14 code cells, and smoke-tested unequal experiment sizes, same-animal/same-type differencing, equal experiment weighting, first-occurrence omission, time alignment, both rendered figures, nine grid panels, labels, axis limits, and PDF targets with synthetic data.

### 2026-07-16 - Selection-line mortality histograms by age

- Slice goal: Compare mortality-record counts across one-month age classes for selection-line fish.
- Passes completed: Extended `temp/fish_analyzes.ipynb` with fish-move filtering and three age histograms for all matching mortality records, overall-bad-shape sacrifices, and found-dead records.
- What changed: The analysis reads the row-5 worksheet header, keeps lines containing `sel`, treats each retained row as one observation, and uses the crossing analysis `AGE_BIN_MONTHS` setting with shared age-bin edges across all three plots.
- Rerun implications: Rerun the loading/settings and mortality cells after changing `AGE_BIN_MONTHS`, `SELECTION_LINE_TOKEN`, or `fish_database.xlsx`.
- Validation performed: Parsed and compiled all 10 notebook code cells; executed the new section against the real workbook; confirmed 320 usable records (112 overall-bad-shape sacrifices and 208 found-dead records), zero invalid ages, shared one-month bins from 0 through 18 months, histogram totals matching the filtered rows, and readable rendered titles, axes, and bin labels for all three plots.

### 2026-07-16 - Age-bin failure stacks by selection line

- Slice goal: Refocus the stacked age-bin histogram from successful crossings to failed crossings.
- Passes completed: Updated `temp/fish_analyzes.ipynb` to summarize failure proportions, stack each line's contribution to failures, and retain total-attempt sample-size labels.
- What changed: Each segment is the line's failed crossings divided by all crossings in that age bin, so the full stack equals the bin's overall failure proportion; bins with attempts but no failures remain labeled empty slots.
- Rerun implications: Rerun the settings, crossing-history, and age-bin cells after changing the bin width, crossing filters, or source workbook.
- Validation performed: Parsed and compiled all notebook cells; executed the real workbook data with 126 eligible crosses, 27 failures across 11 lines, 12 age bins, and zero age/line ambiguities; confirmed stacks equal overall failure proportions, failure and success proportions are complementary, total-attempt labels are correct, three zero-failure bins remain visible, 30-day and 60-day widths work, ambiguous multi-line crosses are excluded, invalid widths fail, and the rendered plot and legend are readable.

### 2026-07-16 - Age-bin success stacks by selection line

- Slice goal: Keep age-bin bar heights equal to overall incross success while showing each selection line's contribution within the bars.
- Passes completed: Updated the age-bin plot in `temp/fish_analyzes.ipynb` to retain one unambiguous line per cross, calculate line-specific success contributions, draw stacked colors, and label total cross attempts.
- What changed: Each segment is the line's successful crossings divided by all crossings in that age bin, so the stack still equals the bin's overall success proportion; ambiguous multi-age or multi-line crosses are excluded and reported.
- Rerun implications: Rerun the settings, crossing-history, and age-bin cells after changing the bin width, crossing filters, or source workbook.
- Validation performed: Parsed and compiled all notebook cells; executed the real workbook data with 126 eligible crosses across 26 lines and zero age/line ambiguities; confirmed 23 lines with successes appear in the stack, stack totals equal overall success proportions, labels equal total attempts, 30-day and 60-day widths work, zero-success bins retain labeled empty slots, multi-line crosses are excluded, invalid widths fail, and the rendered plot and legend are readable.

### 2026-07-16 - Age-binned incross success plot

- Slice goal: Summarize crossing success as a function of fish age without splitting the result by selection line.
- Passes completed: Extended `temp/fish_analyzes.ipynb` with a user-editable 30-day month bin width, cross-level age reduction, a bin summary table, and a histogram-style proportion plot.
- What changed: The new plot pools the existing filtered selection-line cohort, counts each cross once, excludes crosses with multiple distinct known parent ages, and omits empty age classes rather than treating them as unsuccessful.
- Rerun implications: Rerun the settings, crossing-history, and age-bin cells after changing `AGE_BIN_MONTHS`, another crossing filter, or the source workbook.
- Validation performed: Parsed and compiled all notebook cells; executed the real workbook data through the new plot; confirmed 126 eligible unique crosses, zero multi-age exclusions, correct per-bin proportions, 30-day and 60-day widths, rejection of a zero-width setting, and readable rendered axes without line-based encoding.

### 2026-07-16 - Incross success barplot by selection line

- Slice goal: Plot crossing success percentages per selection line while excluding outcrosses.
- Passes completed: Extended `temp/fish_analyzes.ipynb` with a seaborn barplot and line-level success summary.
- What changed: The plot uses the editable `CROSSING_TYPE_FILTER` and `SELECTION_LINE_TOKEN` settings, maps `sel1`/`sel3` families including `TLSel GC` and `TL sel mid`, orders lines by family, and treats `0 (only males)` as an unsuccessful crossing while excluding missing success values.
- Rerun implications: Rerun the settings, filtering, and plotting cells after changing either filter setting or the source workbook.
- Validation performed: Compiled all notebook code cells, rendered the plot with a noninteractive Matplotlib backend, confirmed the default incross run yields 143 filtered records and 28 line summaries, and confirmed changing the type setting to `outcross` changes the result to 6 records and 4 summaries.

### 2026-07-16 - Fish database loading notebook

- Slice goal: Add a temporary notebook entrypoint for inspecting the two multi-sheet fish-information workbooks.
- Passes completed: Added `temp/fish_analyzes.ipynb` with explicit workbook paths, all-sheet loading, missing-file validation, a worksheet shape summary, editable selection-line and crossing-type filters, and a filtered crossing-efficiency table.
- What changed: The notebook loads `crosses.xlsx` and `fish_database.xlsx` into nested dictionaries of pandas DataFrames, reads the four-row-header `Crosses efficiency` sheet, filters rows whose male or female strain contains the configured selection token and whose crossing type matches the configured value, and summarizes selection lines with their tank IDs.
- Rerun implications: Rerun the loading cell whenever either source workbook changes.
- Validation performed: Parsed and syntax-checked the notebook, then executed the loading cell against both current workbooks.

### 2026-07-15 - Multi-experiment LoomAnalysisCR notebook

- Slice goal: Extend the legacy loom-response analyses from one recording to the 2026 shoaling-selection cohort while keeping experiments as equally weighted replicates.
- Passes completed: Added `Analyses/LoomAnalysisCR.ipynb`; extended `functions/joh_loom_helpers.py` with metadata selection, condition-trial alignment, compact extraction, settings-validated per-experiment caches, and cross-experiment summaries.
- What changed: The notebook dynamically selects the current eight 2026 experiments and presents legacy center-distance traces, legacy baseline/response metrics, trial-level velocity traces, trial maximum velocity versus experiment time, and trial maximum velocity by loom side. Dot-plot cells switch between experiment points and aligned condition/trial averages; trace plots always average experiments.
- Rerun implications: The first run reads each selected raw `PositionTxt` recording and creates notebook-specific `csv.gz` caches plus JSON sidecars. Later runs reuse matching caches; set `FORCE_REPROCESS_RAW_DATA=True` to rebuild them deliberately.
- Validation performed: Parsed and compiled all notebook cells, confirmed the live metadata filter selects eight 35-animal experiments with no missing raw paths, and smoke-tested unequal experiment weighting, trial alignment, cache reuse/invalidation, all five plots, both point modes, and averaged point counts with synthetic data. Full raw-recording processing was not run because continued NAS cache access was not authorized.

### 2026-07-15 - Looming animal-response workflow registration

- Slice goal: Register the new `CLfull...` loom-stimulus notebook and reusable helper module in the agentic documentation.
- Passes completed: Added `Analyses/LoomingAnimalResponseAnalysis.ipynb` and `functions/joh_loom_helpers.py` to the notebook stage map and symbol index.
- What changed: Documented the raw embedded-stimulus input, fixed epFrame-150 legacy alignment, no-L/R-mirroring convention, notebook analysis scope, helper ownership, and absence of canonical output files.
- Rerun implications: No analysis rerun required; future agents should inspect the stage map and `functions/joh_loom_helpers.py` before changing loom workflow behavior.
- Validation performed: Parsed the notebook structure and reviewed its headings/imports, inspected all helper entrypoints, and confirmed the documentation references the repository paths and symbols.

### 2026-07-09 - Trajectory heatmap time occupancy

- Slice goal: Change the trajectory-grid heatmap colors from distance traveled per bin to time spent per bin.
- Passes completed: Updated `Analyses/ShoalingTrajectoryGrid_2026.ipynb`.
- What changed: The 5x7 heatmap now bins finite sampled x/y positions with `sample_seconds` weights, so colors show seconds spent per spatial bin while subplot labels and movement metrics still report distance-based speed and zMAD.
- Rerun implications: No pipeline rerun required; rerun the movement heatmap/metrics cell to refresh the displayed and saved PNG/PDF/metrics outputs.
- Validation performed: Parsed the notebook JSON, compiled notebook code cells with Python `ast`, and smoke-tested the heatmap cell on synthetic 35-fish trajectories to confirm stationary occupancy, seconds/bin labels, speed labels, and speed-metric columns.

### 2026-07-09 - Speed distribution zMAD guides

- Slice goal: Replace percentile guides in the trajectory-grid speed distribution plot with robust outlier thresholds.
- Passes completed: Updated `Analyses/ShoalingTrajectoryGrid_2026.ipynb`.
- What changed: The final speed-distribution cell now computes the mean speeds corresponding to movement `zMAD = +3` and `zMAD = -3` from `distance_per_min`, converts them to mm/s, and draws those values as horizontal dotted guide lines instead of 95th-percentile markers.
- Rerun implications: No pipeline rerun required; rerun the movement heatmap/metrics cell and final speed-distribution cell to refresh the displayed and saved figure.
- Validation performed: Parsed the notebook JSON, confirmed stale speed-cell percentile references are absent, and syntax/smoke-checked the edited speed plot cell.

### 2026-07-09 - Seaborn speed distribution cleanup

- Slice goal: Use seaborn to simplify the individual speed distribution plot in the trajectory-grid notebook.
- Passes completed: Updated `Analyses/ShoalingTrajectoryGrid_2026.ipynb`.
- What changed: Added `seaborn` to the notebook imports, replaced the manual jittered scatter/color loop with `sns.stripplot`, retained Matplotlib percentile annotations, and moved genotype sample counts onto the x-axis labels.
- Rerun implications: No pipeline rerun required; rerun the import/settings cell and final speed-distribution cell after `movement_metrics` exists.
- Validation performed: Parsed the notebook JSON, compiled all code cells with Python `ast`, and smoke-executed the speed plot cell on synthetic `movement_metrics` with saving disabled.

### 2026-07-09 - Trajectory-grid readability refactor

- Slice goal: Make the trajectory-grid notebook easier to read by keeping plot logic inside the plot cells.
- Passes completed: Updated `Analyses/ShoalingTrajectoryGrid_2026.ipynb`.
- What changed: Reduced the `## Helpers` code cell to the reused filename helper, inlined one-use trajectory loading, metadata mapping, trajectory-grid plotting, movement-heatmap plotting, and speed-plot logic into their owning notebook cells, and added step-by-step comments for human readers.
- Rerun implications: No data rerun required; rerun the notebook cells to refresh displayed and saved figures.
- Validation performed: Parsed the notebook JSON, compiled all code cells with Python `ast`, confirmed the removed one-use helper names are absent, and smoke-rendered the trajectory grid, movement heatmap grid, and speed plot on synthetic 35-fish data with saving disabled.

### 2026-07-09 - Movement heatmap colorbar spacing

- Slice goal: Move the movement heatmap grid colorbar outside the subplot grid.
- Passes completed: Updated `Analyses/ShoalingTrajectoryGrid_2026.ipynb`.
- What changed: The heatmap grid now reserves a right margin and draws the shared colorbar in a dedicated outer figure axis instead of letting it consume or overlap subplot space.
- Rerun implications: No data rerun required; rerun the movement heatmap cell to refresh the displayed and saved PNG/PDF.
- Validation performed: Parsed the notebook JSON, compiled all code cells with Python `ast`, and smoke-rendered the heatmap helper to confirm the colorbar axis sits outside the grid axes.

### 2026-07-09 - Individual speed distribution plot

- Slice goal: Add a notebook-local plot of individual speed distribution colored by fish genotype.
- Passes completed: Updated `Analyses/ShoalingTrajectoryGrid_2026.ipynb`.
- What changed: Appended a final inline code cell that uses the previous cell's `movement_metrics` table, plots one dot per fish grouped and colored by genotype, draws genotype-specific and overall 95th-percentile reference lines, and optionally saves PNG/PDF plus a speed table when `SAVE_FIGURES=True`.
- Rerun implications: No pipeline rerun required; rerun the movement heatmap/metrics cell and the final speed-distribution cell to refresh the figure for a selected experiment/window.
- Validation performed: Parsed the notebook JSON, compiled all code cells with Python `ast`, and smoke-rendered the new cell on dummy 35-fish trajectory data with a noninteractive Matplotlib backend.

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
