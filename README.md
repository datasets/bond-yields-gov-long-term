<a className="gh-badge" href="https://datahub.io/core/bond-yields-gov-long-term"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25" alt="badge" /></a>

Monthly average US 10-year Treasury constant maturity yield from April 1953 to the present. Values are sourced from the Federal Reserve Bank of St. Louis ([FRED series DGS10](https://fred.stlouisfed.org/series/DGS10)) and expressed as a percentage.

## Data

The dataset contains one row per calendar month. The `Yield` value is the mean of all daily observations published by FRED for that month, rounded to two decimal places.

**Source:** [Market Yield on U.S. Treasury Securities at 10-Year Constant Maturity (DGS10)](https://fred.stlouisfed.org/series/DGS10) — Federal Reserve Bank of St. Louis.

## Preparation

The process is recorded and automated in a Python script:

```bash
pip install -r scripts/requirements.txt
python scripts/process.py
```

## License

Licensed under the [Public Domain Dedication and License][pddl] (assuming either no rights or public domain license in source data).

[pddl]: https://opendatacommons.org/licenses/pddl/
