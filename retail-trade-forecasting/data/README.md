# Data sources and reuse terms

The analysis uses a derived monthly retail-trade dataset. The repository copy is restricted to the common period from January 2005 through March 2025 and contains only aggregated public statistics. It contains no individual-level or company-level records.

## Sources

- **Australia:** Australian Bureau of Statistics, Retail Trade, Australia. Source information: https://www.abs.gov.au/statistics/industry/retail-and-wholesale-trade/retail-trade-australia. Based on ABS data. ABS website material is generally available under the Creative Commons Attribution 4.0 International licence, subject to stated exclusions: https://www.abs.gov.au/website-privacy-copyright-and-disclaimer
- **New Zealand:** Stats NZ, Retail Trade Survey. Source information: https://www.stats.govt.nz/topics/retail-trade. This work includes Stats NZ data licensed for reuse under the Creative Commons Attribution 4.0 International licence: https://www.stats.govt.nz/about-us/copyright/
- **Great Britain:** Office for National Statistics, Retail Sales Index time series: https://www.ons.gov.uk/businessindustryandtrade/retailindustry/datasets/retailsales/current. Source: Office for National Statistics, licensed under the Open Government Licence v3.0: https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **United States:** U.S. Census Bureau, Monthly Retail Trade time-series data: https://www.census.gov/retail/marts/www/timeseries.html. U.S. federal statistical data are reused with source attribution; users should consult the source page and Census data policies for any specific restrictions.

## Transformations

The source extracts were standardised to four fields: month, country, harmonised industry label, and a 2015-based sales index. Duplicate country-industry-month records are averaged. Rows with a missing target are removed. All countries are truncated to the shared end month of March 2025 so the evaluation compares the same time window.

The harmonised industry labels and calculated index fields are analytical transformations. Differences in national classifications and source revisions remain limitations; the combined file should not be treated as an official harmonised statistical release.
