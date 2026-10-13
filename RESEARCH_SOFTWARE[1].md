# Research Software and Reproducible Workflows

This document describes current software-development directions and research-computing practices associated with my agronomy work. It distinguishes **development objectives** from **demonstrated public releases**.

## cropGrowthR — research package in development

**Objective:** Develop an R package to support transparent crop-growth calculations, experimental-design-aware statistical analysis, functional growth modelling and publication-quality reporting in agronomic research.

### Intended components

| Component | Development objective |
| --- | --- |
| Crop-growth calculations | Implement documented growth indices and equations, with consistent units, time intervals and input requirements. |
| Statistical analysis | Respect the experimental design, including replication and treatment/randomisation structures. |
| Functional modelling | Fit and compare suitable crop-growth functions with clear diagnostics and scientific interpretation. |
| Data validation | Detect data-quality problems, missing information, inconsistencies and implausible inputs before analysis. |
| Reproducibility | Maintain traceable calculations, tests, assumptions and example workflows. |
| Reporting | Produce interpretable tables and figures with defensible labels, notes and uncertainty information. |

**Current disclosure:** Multiple structured development stages have been worked through in VS Code using Codex. Their completion is not independent evidence that all features above exist, produce correct results, or meet release-quality standards. The project is not currently linked here as a verified public package release.

### Verification priorities before a public release

- [ ] Confirm the actual implemented functions against source code and reference documentation.
- [ ] Independently reproduce numerical results using known, auditable examples.
- [ ] Test varied experimental designs, edge cases and invalid inputs.
- [ ] Review units, sign conventions, time scaling and missing-data rules.
- [ ] Run package checks, tests and installation in a clean R environment.
- [ ] Benchmark selected methods against trusted existing implementations.
- [ ] Write installation guidance, worked examples, limitations and a changelog.
- [ ] Publish the repository and release information only when independently verified.

*A project link and version number will be added after the public repository and release status are confirmed.*

## Reproducible agronomic analysis workflow

I aim to make research results **auditable rather than merely automated**:

1. **Define the experiment:** Specify scientific hypotheses, experimental units, factors, randomisation and replication.
2. **Audit the data:** Check identifiers, treatment combinations, measurement units, outliers, missingness and impossible values.
3. **Choose the model:** Match estimation and error terms to the experimental design; document justified alternatives.
4. **Inspect assumptions:** Evaluate diagnostics, variance structure and model fit.
5. **Interpret results:** Report effect estimates, uncertainty and appropriate treatment comparisons without overstatement.
6. **Produce research outputs:** Generate reproducible tables, figures, captions and clear method notes.
7. **Validate:** Compare calculations independently and retain code, data provenance and analysis settings where permitted.

## Tools and methods

**Core analytical environment:** R; R Markdown/Quarto; RStudio; VS Code.  
**Assisted development:** Codex in VS Code for R and Python scripting, testing and workflow refinement.  
**Statistical approaches:** Design-appropriate ANOVA and mixed models; diagnostics; multivariate exploration when justified.  
**Communication:** Reproducible manuscripts, publication-style plots and transparent analytical reports.

## Related GitHub material

- [Quarto manuscript tutorial/template](https://github.com/farhan-khalid-git/manuscript-tutoria) — an existing tutorial/template repository, not represented as a standalone original package.
- [GitHub profile repository](https://github.com/farhan-khalid-git/farhan-khalid-git) — home for this profile and the accompanying expertise notes.

[← Return to profile README](README.md)
