<a className="gh-badge" href="https://datahub.io/core/bond-yields-gov-long-term"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25" alt="badge" /></a>

Long term government bond yields.

# Data

## European Union

[ECB - Long-term interest rate statistics for EU Member States] (note this data is also the source for that [provided by Eurostat][eurostat]). As stated on Eurostat site:

> Long term government bond yields are calculated as monthly averages (non seasonally adjusted data). They refer to central government bond yields on the secondary market, gross of tax, with a residual maturity of around 10 years. The bond or the bonds of the basket have to be replaced regularly to avoid any maturity drift. This definition is used in the convergence criteria of the Economic and Monetary Union for long-term interest rates, as required under Article 121 of the Treaty of Amsterdam and the Protocol on the convergence criteria. Data are presented in raw form. Source: European Central Bank (ECB)

[ecb]: http://www.ecb.int/stats/money/long/html/index.en.html
[eurostat]: http://epp.eurostat.ec.europa.eu/tgm/table.do?tab=table&plugin=1&language=en&pcode=teimf050

## Preparation
Process is recorded and automated in python script:

```bash
pip install -r scripts/requirements.txt
python  scripts/prepare.py
```

## Automation
Up-to-date (auto-updates every month) bond-yields-gov-long-term dataset could be found on the datahub.io: https://datahub.io/core/bond-yields-gov-long-term

# License

Licensed under the [Public Domain Dedication and License][pddl] (assuming either no rights or public domain license in source data).

[pddl]: http://opendatacommons.org/licenses/pddl/1.0/

