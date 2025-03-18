import pandas as pd
import numpy as np
import yfinance as yf

# Sample data for 5 different stocks
data = {
    'Stock_A': np.random.normal(0, 1, 100),
    'Stock_B': np.random.normal(0, 1, 100),
    'Stock_C': np.random.normal(0, 1, 100),
    'Stock_D': np.random.normal(0, 1, 100),
    'Stock_E': np.random.normal(0, 1, 100)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate the coefficient of skewness for each stock
skewness = df.skew()

print("Coefficient of Skewness (beta1) for each stock:")
import matplotlib.pyplot as plt

# Define the stock symbols
stocks = ['AAPL', 'MSFT', 'TSLA', 'PLTR']

# Download the stock data
data = yf.download(stocks, start='2020-01-01', end='2023-01-01')['Close']

# Calculate the daily returns
returns = data.pct_change().dropna()

# Calculate the moment coefficient of skewness (beta1) for each stock
beta1_skewness = returns.apply(lambda x: ((x - x.mean())**3).mean() / (x.std()**3))

# Calculate the coefficient of skewness (gamma1) for each stock
gamma1_skewness = returns.skew()

print("Moment Coefficient of Skewness (beta1) for each stock:")
print(beta1_skewness)

print("Coefficient of Skewness (gamma1) for each stock:")
print(gamma1_skewness)

# Plot the moment coefficient of skewness (beta1)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
beta1_skewness.plot(kind='bar', title='Moment Coefficient of Skewness (beta1)')
plt.xlabel('Stocks')
plt.ylabel('Skewness')

# Plot the coefficient of skewness (gamma1)
plt.subplot(1, 2, 2)
gamma1_skewness.plot(kind='bar', title='Coefficient of Skewness (gamma1)')
plt.xlabel('Stocks')
plt.ylabel('Skewness')

plt.tight_layout()
plt.show()
# Calculate the kurtosis for each stock
kurtosis = returns.kurtosis()

print("Kurtosis for each stock:")
print(kurtosis)

# Plot the kurtosis
plt.figure(figsize=(10, 5))
kurtosis.plot(kind='bar', title='Kurtosis')
plt.xlabel('Stocks')
plt.ylabel('Kurtosis')
plt.show()