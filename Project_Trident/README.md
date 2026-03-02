## Project_Trident

Project_Trident contains two primary documents and their supporting datasets. `Capital_Flow_Opacity_Framework.md` documents three mechanisms that enable capital flows to bypass accountability infrastructure: (a) technical vulnerabilities in cross-border payment systems including NULL field defaults and cover payment blind spots, sourced from Oracle Banking documentation and FATF guidance; (b) codified regulatory exemptions including CFIUS §800.307 passive LP exemption, CHIPS Act country exclusions for Gulf states, and documented FARA non-enforcement patterns; (c) administrative timing — the statistical correlation between friction events and compliance events, verified at r=0.6196 with a 2-week index lag (actual median: 7 days · v10.3 High-Resolution, backfill n=66) and cross-referenced against the main dashboard.

`Ritual_Timing_Signal_Analysis.md` is a statistical test of whether rare, controllable ritual/religious events cluster with policy events above a holiday baseline. Findings: 50.7% proximity vs 19.9% holiday baseline, 3.5x ratio, p=0.002 Mann-Whitney U test. This module is explicitly flagged as requiring further independent scrutiny and is not considered a primary finding of the project.

All datasets are independently verifiable using `Veriify_Trident_Analysis.py`.
