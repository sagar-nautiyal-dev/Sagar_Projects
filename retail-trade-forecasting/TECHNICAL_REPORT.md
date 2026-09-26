# Retail trade forecasting case study

## Objective

The project evaluates whether recent retail-index history, seasonality, country, and industry can predict the next observed monthly retail-sales index across four national markets.

## Data

The analysis combines aggregated public statistics from the Australian Bureau of Statistics, Stats NZ, the Office for National Statistics, and the U.S. Census Bureau. Each series is converted to a shared schema and restricted to January 2005 through March 2025, the latest month available for every country in the supplied extracts.

## Method

Lag-one, lag-twelve, trailing twelve-month mean, seasonal, country, industry, and time features are calculated without using future observations. Model selection uses three expanding chronological validation windows. January 2024 through March 2025 remains untouched until the final comparison.

Ridge regression and Random Forest are compared with a seasonal-naive baseline. The primary measures are R², root mean squared error, and mean absolute error.

## Results

The best final-test model was **Random Forest**, with R² **0.977**, RMSE **6.678**, and MAE **4.479**. The seasonal-naive benchmark produced R² **0.969**, RMSE **7.751**, and MAE **5.340**.

These results replace the earlier random-split interpretation. The chronological design provides a more realistic estimate of performance on later months and avoids presenting near-perfect random-split results as general forecasting performance.

Performance is uneven across countries. United States recorded a country-level R² of **-0.960** with RMSE **2.199**. The low absolute error but negative R² means the model did not beat a country-mean benchmark for that low-variance test slice.

## Limitations

National survey definitions and industry classifications are not identical. The analysis models harmonised indices rather than raw revenue, uses observed lag values for one-step-ahead prediction, and does not estimate causal effects. Agency revisions may change historical observations. Country-level results should be reviewed alongside the overall score.

## Reproduction

The executed notebook contains the complete data checks, feature construction, validation design, model selection, evaluation tables, and charts. Pinned dependencies and a self-contained data fallback allow the analysis to be rerun without credentials.
