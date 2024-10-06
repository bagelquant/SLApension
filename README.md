# SLApension

Portfolio optimization for McGill competition 2024


## Portfolio level

### Asset Allocation Strategy

Using long-term historical data for indexes of different asset classes, we will use the mean-variance optimization to find the optimal weights for each asset class. 

Things to consider:

- Optimization boundaries (Only need to finish this model for the proposal)
    - Target return
    - Risk tolerance (bounds on the variance)
    - Constraints on the weights (e.g. no short selling)
- Index choice -> compare different indexes for each asset class
- Time horizon -> match the time horizon of the competition

### Rebalancing Strategy

Using the Black-Litterman model, we will adjust the weights of the portfolio based on the market conditions. 

Things to consider:
- rebalancing frequency
- Black-Litterman model parameters
- Market conditions -> how to adjust the weights based on the market conditions

### Risk Management

- Risk evaluation metrics:
    - Value at Risk (VaR)
    - Conditional Value at Risk (CVaR)
    - Maximum Drawdown
    - Sharpe Ratio
- Determine adjusting strategy when the risk exceeds a certain threshold -> should compare to market

### Performance Evaluation

- Backtesting the strategy using historical data
- Compare the performance of the strategy with the benchmark
- Sensitivity analysis on the parameters

### Construction of the Portfolio

## Asset level

### Within asset class optimization

- fixed income: match the duration of the bond with the expected customer's time horizon
- equity: use the factor model to find the optimal weights for each stock or funds
- others: a mean-variance optimization for the asset class

### Asset Selection

Using asset pooling, we will select the best assets for each asset class.

- First pool: select the best assets based on historical data, a negative screen for the assets 
- Second pool: Do in-depth analysis on the assets in the first pool, select the best assets based on the analysis
- Third pool(invest-ready): Investment committee will select the best assets based on the analysis of the second pool, the frequency of the selection will be determined by the rebalancing strategy

### Risk Management

- Risk evaluation metrics:
    - Value at Risk (VaR)
    - Conditional Value at Risk (CVaR)
    - Maximum Drawdown
    - Sharpe Ratio
- Exceeding the risk threshold
    - Adjust the weights of the assets
    - Continue monitoring the risk level
    - Remove the asset from the pool if the risk level is too high

