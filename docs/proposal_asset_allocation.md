## Assset Allocation and Portfolio Mentaiance

> length: 1 paragraph

Quick intro to out methodology:

- Portfolio level -> Mean-variance optimization using indexes of different asset classes
- Asset level
    - For some asset class will have a different optimization strategy
    - Asset selection process


### Alocation methodology

2 paragraph on mean-variance optimization

- Optimization boundaries
    - Target return
    - Risk tolerance
    - Cash constraint
- Results

1 paragraph on why choose this indexes and time horizon

### Rebalancing Strategy

1 paragraph on Rebalancing and Macroeconomic teams who will be responsible for the provide market views.

1 paragraph on Black-Litterman model

#### Notes -> What is Black-Litterman model

step1: Calculate the implied returns (Expected returns), normally using the CAPM model to calculate the expected returns, CAPM:

$$ E(R_i) = R_f + \beta_i(E(R_m) - R_f)$$

step2: Give a view on the market, for example, you think asset A will outperform to 10% with confidence level 70%, then you can adjust the expected return of asset A and B based on this view.

example:

- Asset A expected return: 5%
- Asset A expected return after view: 5% * 0.3 + 10% * 0.7 = 7.5%

#### How we use Black-Litterman model

1. Use our portfolio historical data as $E(R_m)$, and calculate the implied returns for each asset class
2. Macroeconomic team will provide the market views, will give a confidence level of three conditions: outperform, underperform, and neutral
3. outperform will increase the expected return by 5%, underperform will decrease the expected return by 10%, and neutral will keep the expected return the same

### Risk Management

1 paragraph on Risk management

1. Monitoring Daily spread(Portfolio - benchmark), benchmark = CPI + 3%
2. Calculate the VaR, max drawdown, and Sharpe ratio for the daily spread
3. if the daily spread exceeds the threshold for 20 days, we will adjust the portfolio weights 

### Performance Evaluation

1 paragraph on Performance evaluation and expected return

### Construction of the Portfolio -> Optional, if we have enough space

1 paragraph on explain the steps for entering the market

## Asset level

1 paragraph on the different optimization strategy for each asset class

1 paragraph on the asset selection process:
- First pool: select the best assets based on historical data, a negative screen for the assets
- Second pool: Do in-depth analysis on the assets in the first pool, select the best assets based on the analysis
- Third pool(invest-ready): Investment committee will select the best assets based on the analysis of the second pool, the frequency of the selection will be determined by the rebalancing strategy

1 paragraph on the risk management -> almost the same as the portfolio level



