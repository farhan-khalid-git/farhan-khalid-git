# Research Software & Reproducible Agronomic Analysis

I use reproducible analytical workflows to connect agronomic experiments, statistical inference and publication-oriented reporting.

## cropGrowthR — package development and validation

**cropGrowthR** is an R-package development effort centred on crop-growth analysis. Its planned scope includes documented growth indices, growth-function fitting, transparent diagnostics, design-appropriate modelling and interpretable tables and figures.

**Status:** Under development and validation. This page does not claim an independently validated public release, complete feature coverage or availability through CRAN. A working repository URL and installation instructions will be added after the source and release status have been verified.

### Release-readiness checklist

- [ ] Inventory implemented functions and define their inputs, outputs and units.
- [ ] Validate numerical calculations against independent references.
- [ ] Test growth functions on suitable repeated-measure experiments.
- [ ] Evaluate error structures, treatment comparisons and model diagnostics.
- [ ] Add package documentation, examples and reproducible vignettes.
- [ ] Run automated tests and R package checks in clean environments.
- [ ] Confirm licensing, authorship, citation metadata and version history.
- [ ] Publish a tested public repository and document known limitations.

## Analysis quality principles

1. Validate raw data, factor coding, missingness, measurement units and experimental units.
2. Match statistical models to randomisation, blocking and replication.
3. Diagnose model assumptions, heterogeneity and dependence structures.
4. Report treatment contrasts, uncertainty and interactions transparently.
5. Create scientifically relevant visualisations, not graphics for decoration.
6. Preserve scripts and provenance so permitted analyses can be reproduced.

## Tooling

| Tool | Application |
| --- | --- |
| **R and RStudio** | Statistical analysis, agronomic modelling and graphical reporting |
| **R Markdown / Quarto** | Reproducible reports and manuscript workflows |
| **VS Code + Codex** | AI-assisted coding, validation scripts, code review and workflow refinement |
| **Python-assisted scripting** | Supporting data and modelling tasks, with explicit scientific checks |
| **GitHub** | Version control, documentation and collaborative development |

## Other public repositories

- [Quarto manuscript tutorial/template](https://github.com/farhan-khalid-git/manuscript-tutoria) — an existing tutorial-based repository, not presented as an independently released scientific package.
- [GitHub profile and academic portfolio](https://github.com/farhan-khalid-git/farhan-khalid-git).

[Statistical expertise](STATISTICAL_EXPERTISE.md) · [← Back to GitHub profile](README.md)
