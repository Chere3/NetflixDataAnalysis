# ROADMAP

## Quick wins (1-2 weeks)
- [ ] Add reproducible environment (`requirements.txt`) and execution guide.
- [ ] Add data quality validation script for schema + null checks.
- [ ] Add CI workflow to run validation script on pull requests.
- [ ] Document notebook execution order and expected outputs.

## Medium initiatives (2-6 weeks)
- [ ] Convert notebooks to parameterized pipelines.
- [ ] Add tests for transformation utilities and feature engineering steps.
- [ ] Add dashboard-ready export datasets in `data/processed`.

## Big bets (1-3 months)
- [ ] Add predictive modeling track (retention/engagement proxies).
- [ ] Package project as a lightweight analytics template for portfolio reuse.
- [ ] Integrate automated EDA report generation.

## Strategic rewrites
- [ ] Migrate notebook-first workflow to modular Python package (`src/`).
- [ ] Introduce data contracts and versioned dataset snapshots.
- [ ] Add orchestrated pipeline (Dagster/Prefect) for repeatable runs.
