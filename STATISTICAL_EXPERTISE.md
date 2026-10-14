# Experimental Design, Statistical Analysis & Research Modelling

**Focus:** Valid inference for agronomic experiments, supported by reproducible R workflows and scientific interpretation.

## Study design comes first

A defensible analysis begins with the actual experimental unit, randomisation, factors, blocking and replication. The analysis and error terms must follow the design—not simply the column names in a spreadsheet.

| Research situation | Relevant approach | Reporting considerations |
| --- | --- | --- |
| Completely randomised experiments | CRD-based ANOVA or suitable regression | Independent units, diagnostics and treatment contrasts |
| Field block experiments | RCBD and factorial RCBD analyses | Block effects, interactions, effect estimates and uncertainty |
| Split-plot / split-split-plot trials | Appropriate mixed models and correct error strata | Whole-plot and subplot randomisation; denominator degrees of freedom |
| Multi-year experiments | Combined or hierarchical modelling when justified | Year effects, treatment interactions, variance assumptions |
| Repeated crop measurements | Longitudinal models or growth functions | Repeated-measure dependence and biological sampling structure |
| Multiple correlated outcomes | PCA, clustering or heatmaps where justified | Standardisation, missingness, interpretation and limitations |

## Analytical workflow

1. **Audit the dataset:** Confirm identifiers, factor levels, units, missing observations, impossible values and treatment completeness.
2. **Reconstruct the experiment:** Write down experimental units, design, randomisation, blocking and measurement timings.
3. **Choose estimands and models:** Specify biologically meaningful effects and design-aware error structure before fitting.
4. **Assess assumptions:** Inspect residuals, distribution, dispersion, heterogeneity and relevant model-fit indicators.
5. **Compare treatments responsibly:** Report interactions and estimated marginal means; use LSD or other multiple-comparison methods only where justified.
6. **Quantify uncertainty:** Present estimates, intervals and meaningful effect sizes rather than significance letters alone.
7. **Validate results:** Cross-check model outputs, units, numerical stability and reproducibility.
8. **Report transparently:** Provide labelled tables, figure captions, methodological notes and scripts where sharing is permitted.

## Computing environment

- **R/RStudio:** Data analysis, mixed modelling, visualisation and reproducible reporting.
- **R Markdown/Quarto:** Rebuildable analytical documents and manuscript-oriented outputs.
- **VS Code with Codex:** AI-assisted development, debugging and code review for R and Python research workflows.
- **Python:** Used within assisted research-computing workflows; not presented as independently certified proficiency.

## Practical reporting principles

- Choose visualisations to answer an analytical question, not merely to display descriptive statistics.
- Do not use PCA or confidence ellipses to compensate for insufficient independent replication.
- Distinguish modelled and measured values, and describe relevant limitations.
- Retain raw-data provenance and do not report synthetic or inferred observations as actual measurements.
- Treat auto-generated analysis as preliminary until scientifically and statistically verified.

## Example applications

Field-crop management studies involving wheat, rice and maize; drought and nutrient-management experiments; microbial inoculation; intercropping; and growth responses measured through time.

[Detailed agronomy expertise](RESEARCH_EXPERTISE.md) · [Software and reproducibility](RESEARCH_SOFTWARE.md) · [← Profile](README.md)
