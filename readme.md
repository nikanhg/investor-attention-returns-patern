# Investor Attention and Stock Market Dynamics

## Overview

This research investigates the long-term and short-term effects of investor attention on stock returns and volatility. Our aim is to understand how investor attention, measured through metrics such as the number of downloads of filings and Google Search Volume Index (SVI), influences stock market dynamics.

## Metrics

We utilize the following metrics to capture patterns of investor attention:

- Number of downloads of filings from the EDGAR database.
- Google Search Volume Index (SVI).

Our analysis seeks to uncover the relationship between stock returns and volume, across various lags, with these investor attention metrics.

## Hypothesis

Our study is driven by several hypotheses regarding the impact of investor attention:

1. A causal relationship exists between the pairs of Returns & SVI, Returns & EDGAR, Volume & SVI, and Volume & EDGAR for the majority of companies.
2. Differences exist between low and high capitalization companies in how their stock returns and volume are influenced by SVI and EDGAR.
3. SVI has a more pronounced impact on stock returns and volume compared to EDGAR downloads.
4. It takes less than 3 weeks (3 lags) to capture the stock performance response to an investor attention shock, with the response dissipating over the long term (> 3 months).
5. Returns are predictable through metrics of investor attention by identifying patterns of change in investor attention.
6. Investor attention positively affects stock performance, and this trend can be predicted.

## Final Results

- **H1:** Causal relationships were identified between the pairs Returns & SVI (12.76%), Returns & EDGAR (5.17%), Volume & SVI (24.13%), and Volume & EDGAR (17.24%).
- **H2:** Significant differences were found between high and low capitalization companies regarding the causality for Returns & EDGAR, Volume & EDGAR, and Volume & SVI.
- **H3:** In the short term, a stronger correlation exists between the SVI index and weekly return compared to EDGAR downloads. SVI has a greater impact on stock returns and volume for high capitalization companies, while the opposite is true for low capitalization companies.
- **H4:** It takes 5 weeks (5 lags) to capture the response of stock performance to investor attention shock, with the response dissipating over the long term (3 months).
- **H5:** The highest accuracy achieved was 60%, indicating that returns are not predictable via metrics of investor attention.
- **H6:** Investor attention significantly affects performance, not just positively. The best results were obtained when returns were labeled based on extremeness.

## File Structure

- `Data` folder: Contains all the data used in the research.
- `data-analysis`: Visual analysis and Granger causality test.
- `data-extraction`: Data extraction for companies, EDGAR download, and SVI.
- `model`: The VAR and LSTM regression and classification models.
- `methods`: Global methods used in the research.
- `results`: Results from the statistical tests and machine learning models.

"""
