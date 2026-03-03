# Update Script Maintenance Report

Date: 2026-03-03

- Ran updater using `python scripts/process.py` in a local venv.
- Fixed hardcoded FRED query dates in `scripts/process.py`:
  - `coed` now uses `current_date`
  - `vintage_date` now uses `current_date`
- Regenerated `data/us-10y.csv` with current monthly values.
