"""
Optimization module
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def get_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path, index_col=0)


def cal_return_cov(raw_data: pd.DataFrame) -> tuple[pd.Series, pd.DataFrame]:
    drifts = raw_data / raw_data.shift(1) - 1
    expected_return = drifts.mean()
    expected_return = (expected_return + 1)**12 - 1
    cov = drifts.cov()
    return expected_return, cov


def cal_portfolio_return(weights: pd.Series, expected_return: pd.Series) -> float:
    weights.index = expected_return.index
    return weights.T.dot(expected_return)


def cal_portfolio_variance(weights: pd.Series, cov: pd.DataFrame) -> float:
    weights.index = cov.index
    return weights.T.dot(cov).dot(weights)


def generate_random_weights(assets_number: int) -> pd.Series:
    return pd.Series(np.random.rand(assets_number))


def plot_random_portfolios(porfolios_return: list[float], porfolios_variance: list[float]) -> None:
    plot_df = pd.DataFrame({"Return": porfolios_return, "Variance": porfolios_variance})
    plot_df.plot.scatter(x="Variance", y="Return")
    plt.show()
    

def main():
    raw_data = get_data("data/raw_data.csv")
    expected_return, cov = cal_return_cov(raw_data)

    porfolios_return = []
    porfolios_variance = []
    for i in range(10000):
        weights = generate_random_weights(4)
      
        porfolios_return.append(cal_portfolio_return(weights, expected_return)) 
        porfolios_variance.append(cal_portfolio_variance(weights, cov))
    
    plot_random_portfolios(porfolios_return, porfolios_variance)


if __name__ == "__main__":
    main()

