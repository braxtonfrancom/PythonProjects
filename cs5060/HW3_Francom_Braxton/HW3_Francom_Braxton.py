#PART 1
import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
import seaborn as sns
from fitter import Fitter


class European_Call_Payoff:

    def __init__(self, strike):
        self.strike = strike

    def get_payoff(self, stock_price):
        if stock_price > self.strike:
            return stock_price - self.strike
        else:
            return 0


class GeometricBrownianMotion:

    def simulate_paths(self):
        while(self.T - self.dt > 0):
            dWt = np.random.normal(0, math.sqrt(self.volatility))  # Brownian motion
            dYt = self.drift*self.dt + self.volatility*dWt  # Change in price
            self.current_price += dYt  # Add the change to the current price
            self.prices.append(self.current_price)  # Append new price to series
            self.T -= self.dt  # Account for the step in time

    def __init__(self, initial_price, drift, volatility, dt, T):
        self.current_price = initial_price
        self.initial_price = initial_price
        self.drift = drift
        self.volatility = volatility
        self.dt = dt
        self.T = T
        self.prices = []
        self.simulate_paths()


class BetaMotion:

    def simulate_paths(self):
        while(self.T - self.dt > 0):
            dWt = np.random.beta(20,8) - .25  # Beta motion with shift to left of .25
            dYt = self.drift*self.dt + self.volatility*dWt  # Change in price
            # print("Change in price: {0}", dYt)
            self.current_price += dYt  # Add the change to the current price
            self.prices.append(self.current_price)  # Append new price to series
            self.T -= self.dt  # Account for the step in time

    def __init__(self, initial_price, drift, volatility, dt, T):
        self.current_price = initial_price
        self.initial_price = initial_price
        self.drift = drift
        self.volatility = volatility
        self.dt = dt
        self.T = T
        self.prices = []
        self.simulate_paths()


# Model Parameters
paths = 5000
initial_price = 100
drift = .01
volatility = 0.7
dt = 1/365
T = 1
price_paths = []

# Generate a set of sample paths
for i in range(0, paths):
    price_paths.append(BetaMotion(initial_price, drift, volatility, dt, T).prices)

call_payoffs = []
final_prices = []
ec = European_Call_Payoff(100)
risk_free_rate = .01
for price_path in price_paths:
    call_payoffs.append(ec.get_payoff(price_path[-1])/(1 + risk_free_rate))
    final_prices.append(price_path[-1])

# Plot the set of generated sample paths
for price_path in price_paths:
    plt.plot(price_path)
plt.xlabel('Days')
plt.ylabel('Price')
plt.title("Simulations of Stock Price Based on Beta Distribution")
plt.show()

print(f"Average stock price after {int(1 / dt) * T} days: $", np.average(final_prices))
print("\nAverage payoff(option block of 100): $", np.average(call_payoffs)*100)  # Options are in blocks of 100
print("Cost of option: $", np.average(call_payoffs))






#PART 2

stock1_data = pd.read_csv("stock1.csv", header=None)
stock2_data = pd.read_csv("stock2-1.csv", header=None)

change_in_price_stock1 = stock1_data.diff().dropna()
change_in_price_stock2 = stock2_data.diff().dropna()

sns.set_style('white')
sns.set_context("paper", font_scale = 2)


sns.displot(data=change_in_price_stock1, kind="hist", bins=100, height=6, aspect=1.5)
plt.xlabel('Change in stock price from previous day')
plt.ylabel('Number of Occurrences')
plt.show()


sns.displot(data=change_in_price_stock2, kind="hist", bins=100, height=6, aspect=1.5)
plt.xlabel('Change in stock price from previous day')
plt.ylabel('Number of Occurrences')
plt.show()


numPyArrayStock1 = change_in_price_stock1.values
numPyArrayStock2 = change_in_price_stock2.values

f = Fitter(numPyArrayStock1,
           distributions=['gamma', 'lognorm', "beta", "burr", "norm"])
f.fit()
f.summary()
plt.show()
best = f.get_best('sumsquare_error')
fitted = f.fitted_param["beta"]
print("The best distributions and parameters for stock1.csv are:")
print(best)

print("The parameters used for stock1.csv's beta distribution are:")
print(fitted)


#Now same thing for stock2
f2 = Fitter(numPyArrayStock2,
           distributions=['gamma', 'lognorm', "beta", "burr", "norm"])
f2.fit()
f2.summary()
plt.show()
best2 = f2.get_best('sumsquare_error')
fitted2 = f.fitted_param["norm"]
print("The best distributions and parameters for stock2-1.csv are:")
print(best2)

print("The parameters used for stock2-1.csv's normal distribution are:")
print(fitted2)





#Last part of part 2:
average_prices = (stock1_data + stock2_data) / 2   # Calculate the average price for each day
max_prices = pd.concat([stock1_data, stock2_data], axis=1).max(axis=1)    # Calculate the max price for each day

class GeometricBrownianMotion:

    def simulate_paths(self):
        while(self.T - self.dt > 0):
            dWt = np.random.normal(0, math.sqrt(self.volatility))  # Brownian motion
            dYt = self.drift*self.dt + self.volatility*dWt  # Change in price
            self.current_price += dYt  # Add the change to the current price
            self.prices.append(self.current_price)  # Append new price to series
            self.T -= self.dt  # Account for the step in time

    def __init__(self, initial_price, drift, volatility, dt, T):
        self.current_price = initial_price
        self.initial_price = initial_price
        self.drift = drift
        self.volatility = volatility
        self.dt = dt
        self.T = T
        self.prices = []
        self.simulate_paths()

class BetaMotion:

    def simulate_paths(self):
        while(self.T - self.dt > 0):
            dWt = np.random.beta(20, 8) - .25  # Beta motion with shift to left of .25
            dYt = self.drift*self.dt + self.volatility*dWt  # Change in price
            self.current_price += dYt  # Add the change to the current price
            self.prices.append(self.current_price)  # Append new price to series
            self.T -= self.dt  # Account for the step in time

    def __init__(self, initial_price, drift, volatility, dt, T):
        self.current_price = initial_price
        self.initial_price = initial_price
        self.drift = drift
        self.volatility = volatility
        self.dt = dt
        self.T = T
        self.prices = []
        self.simulate_paths()

# Model Parameters
paths = 5000
initial_price = average_prices.iloc[0, 0]
drift = .01
volatility = 0.7
dt = 1/365
T = 1
price_paths = []

# Generate a set of sample paths
for i in range(0, paths):
    price_paths.append(GeometricBrownianMotion(initial_price, drift, volatility, dt, T).prices)

call_payoffs = []
final_prices = []
ec = European_Call_Payoff(100)
risk_free_rate = .01
for price_path in price_paths:
    call_payoffs.append(ec.get_payoff(price_path[-1])/(1 + risk_free_rate))
    final_prices.append(price_path[-1])

# Plot the set of generated sample paths
for price_path in price_paths:
    plt.plot(price_path)
plt.xlabel('Days')
plt.ylabel('Price')
plt.title("Simulations of stock price - avg of stock1 and stock2")
plt.show()

print(f"Average stock price after {int(1 / dt) * T} days: $", np.average(final_prices))
print("\nAverage payoff(option block of 100): $", np.average(call_payoffs)*100)  # Options are in blocks of 100
print("Cost of option: $", np.average(call_payoffs))





max_prices = pd.concat([stock1_data, stock2_data], axis=1).max(axis=1)    # Calculate the max price for each day


class GeometricBrownianMotion:

    def simulate_paths(self):
        while(self.T - self.dt > 0):
            dWt = np.random.normal(0, math.sqrt(self.volatility))  # Brownian motion
            dYt = self.drift*self.dt + self.volatility*dWt  # Change in price
            self.current_price += dYt  # Add the change to the current price
            self.prices.append(self.current_price)  # Append new price to series
            self.T -= self.dt  # Account for the step in time

    def __init__(self, initial_price, drift, volatility, dt, T):
        self.current_price = initial_price
        self.initial_price = initial_price
        self.drift = drift
        self.volatility = volatility
        self.dt = dt
        self.T = T
        self.prices = []
        self.simulate_paths()

class BetaMotion:

    def simulate_paths(self):
        while(self.T - self.dt > 0):
            dWt = np.random.beta(20, 8) - .25  # Beta motion with shift to left of .25
            dYt = self.drift*self.dt + self.volatility*dWt  # Change in price
            self.current_price += dYt  # Add the change to the current price
            self.prices.append(self.current_price)  # Append new price to series
            self.T -= self.dt  # Account for the step in time

    def __init__(self, initial_price, drift, volatility, dt, T):
        self.current_price = initial_price
        self.initial_price = initial_price
        self.drift = drift
        self.volatility = volatility
        self.dt = dt
        self.T = T
        self.prices = []
        self.simulate_paths()

# Model Parameters
paths = 5000
initial_price = max_prices.iloc[0]
drift = .01
volatility = 0.7
dt = 1/365
T = 1
price_paths = []

# Generate a set of sample paths
for i in range(0, paths):
    price_paths.append(GeometricBrownianMotion(initial_price, drift, volatility, dt, T).prices)

call_payoffs = []
final_prices = []
ec = European_Call_Payoff(100)
risk_free_rate = .01
for price_path in price_paths:
    call_payoffs.append(ec.get_payoff(price_path[-1])/(1 + risk_free_rate))
    final_prices.append(price_path[-1])

# Plot the set of generated sample paths
for price_path in price_paths:
    plt.plot(price_path)
plt.xlabel('Days')
plt.ylabel('Price')
plt.title("Simulations of stock price - max of stock1 and stock2")
plt.show()

print(f"Max stock price after {int(1 / dt) * T} days: $", np.average(final_prices))
print("\nAverage payoff(option block of 100): $", np.average(call_payoffs)*100)  # Options are in blocks of 100
print("Cost of option: $", np.average(call_payoffs))


