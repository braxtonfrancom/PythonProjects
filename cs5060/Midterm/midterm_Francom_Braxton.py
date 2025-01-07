import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#QUESTION 1.1
print("\nQUESTION 1.1 \n")

def bin_processor(value):
    if value >= 998:
        return "EHP"
    elif value >= 910:
        return "Class 7"
    elif value >= 670:
        return "Class 5"
    else:
        return "Class 3"

def simulate_one_day():
    processors = [random.uniform(1, 1000) for _ in range(1000)]
    binned_processors = [bin_processor(value) for value in processors]
    return binned_processors.count("EHP")

def run_simulation(num_days):
    ehp_per_day = []
    for day in range(1, num_days + 1):
        ehp_count = simulate_one_day()
        ehp_per_day.append(ehp_count)
    return ehp_per_day

simulation_results = run_simulation(50)

plt.plot(range(1, 51), simulation_results, marker='o')
plt.title('Daily Distribution of Simulated EHP Processors')
plt.xlabel('Day')
plt.ylabel('Number of EHP Processors')
plt.grid(True)
plt.show()











#QUESTION 1.2
print("\nQUESTION 1.2 \n")

def bin_processor(value):
    if value >= 998:
        return "EHP"
    elif value >= 910:
        return "Class 7"
    elif value >= 670:
        return "Class 5"
    else:
        return "Class 3"

def simulate_one_day():
    processors = [random.uniform(1, 1000) for _ in range(1000)]
    binned_processors = [bin_processor(value) for value in processors]
    return binned_processors.count("EHP")

def run_simulation(num_days):
    ehp_per_day = []
    avg_ehp_processors = []
    total_ehp = 0
    for day in range(1, num_days + 1):
        ehp_count = simulate_one_day()
        ehp_per_day.append(ehp_count)
        total_ehp += ehp_count
        avg_ehp = total_ehp / day
        avg_ehp_processors.append(avg_ehp)
        if day > 370 and avg_ehp_processors[-1] == avg_ehp_processors[-2]:
            break
    return avg_ehp_processors

avg_ehp_processors = run_simulation(500)

plt.plot(range(1, len(avg_ehp_processors) + 1), avg_ehp_processors, marker='o')
plt.title('Performance of Simulated EHP Processors over Time')
plt.xlabel('Day')
plt.ylabel('Average Number of EHP Processors')
plt.grid(True)
plt.show()










#QUESTION 1.3
print("\nQUESTION 1.3 \n")

def calculate_reward(value):
    if value < 998:
        return 0
    else:
        return 5000 * (value - 997) ** 2

num_iterations = 1000
num_days = 50
num_processors_per_day = 1000
stopping_rule_threshold = 0.9
reward_percentages = []

for iteration in range(num_iterations):
    processor_values = np.random.uniform(1, 1000, size=(num_days, num_processors_per_day))
    rewards = np.array([calculate_reward(value) for value in processor_values.flatten()])
    rewards = rewards.reshape((num_days, num_processors_per_day))
    cumulative_rewards = np.cumsum(rewards, axis=1)
    stop_indices = np.argmax(cumulative_rewards > stopping_rule_threshold * cumulative_rewards[:, -1][:, np.newaxis], axis=1)
    reward_percentage = np.mean(stop_indices > 0)
    reward_percentages.append(reward_percentage)

plt.figure(figsize=(8, 6))
plt.hist(reward_percentages, bins=20, color='skyblue', edgecolor='black')
plt.axvline(x=np.mean(reward_percentages), color='red', linestyle='dashed', linewidth=1)
plt.xlabel('Percentage of Days Stopped Early')
plt.ylabel('Frequency')
plt.title('Performance of Stopping Rule with Reward Function')
plt.grid(True)
plt.show()









#QUESTION 1.4
print("\nQUESTION 1.4 \n")

def calculate_reward(value):
    if value < 998:
        return 0
    else:
        return 5000 * (value - 997) ** 2

num_iterations = 1000
num_days = 50
num_processors_per_day = 1000
stopping_rule_threshold = 0.9
reward_percentages = []
success_rates = [0.48, 0.33, 0.14, 0.05]
binning_proportions = [0.67, 0.24, 0.088, 0.002]

total_processors = sum(binning_proportions)
updated_success_rates = [rate * proportion / total_processors for rate, proportion in
                         zip(success_rates, binning_proportions)]

for iteration in range(num_iterations):
    processor_values = np.random.uniform(1, 1000, size=(num_days, num_processors_per_day))
    rewards = np.array([calculate_reward(value) for value in processor_values.flatten()])
    rewards = rewards.reshape((num_days, num_processors_per_day))
    cumulative_rewards = np.cumsum(rewards, axis=1)

    stop_indices = np.argmax(cumulative_rewards > stopping_rule_threshold * cumulative_rewards[:, -1][:, np.newaxis], axis=1)
    reward_percentage = np.mean(stop_indices > 0)
    reward_percentages.append(reward_percentage)

plt.figure(figsize=(8, 6))
plt.hist(reward_percentages, bins=20, color='skyblue', edgecolor='black')
plt.axvline(x=np.mean(reward_percentages), color='red', linestyle='dashed', linewidth=1)
plt.xlabel('Percentage of Days Stopped Early')
plt.ylabel('Frequency')
plt.title('Performance of Stopping Rule with Reward Function')
plt.grid(True)
plt.show()











#QUESTION 2.1
print("\nQUESTION 2.1 \n")

distributions = {
    'area1': lambda size: np.random.beta(2, 2, size) + 1,
    'area2': lambda size: np.random.beta(3, 7, size) * 3,
    'area3': lambda size: np.random.normal(2.4, 1.8, size),
    'area4': lambda size: np.random.uniform(-1, 4, size),
    'area5': lambda size: np.random.normal(0, 9, size),
    'area6': lambda size: np.random.beta(7, 3, size) + 2,
    'area7': lambda size: np.random.uniform(0, 4, size),
    'area8': lambda size: np.random.beta(3, 7, size) * 2,
    'area9': lambda size: np.random.normal(2, 1.4, size),
    'area10': lambda size: np.random.normal(1.3, 7, size)
}

num_months = 24
monthly_values = {area: [] for area in distributions}

for month in range(num_months):
    for area, dist_func in distributions.items():
        values = dist_func(1)
        monthly_values[area].extend(values)

cumulative_values = {area: np.cumsum(values) for area, values in monthly_values.items()}

plt.figure(figsize=(12, 8))
for area, values in cumulative_values.items():
    plt.plot(range(1, num_months + 1), values, label=area)

plt.title('Cumulative Mineral Value Over 2-Year Pilot Study')
plt.xlabel('Months')
plt.ylabel('Cumulative Value')
plt.legend()
plt.grid(True)
plt.show()









#QUESTION 2.2
print("\nQUESTION 2.2 \n")

distributions = {
    'area1': np.random.beta(2, 2, 24) + 1,
    'area2': np.random.beta(3, 7, 24) * 3,
    'area3': np.random.normal(2.4, 1.8, 24),
    'area4': np.random.uniform(-1, 4, 24),
    'area5': np.random.normal(0, 9, 24),
    'area6': np.random.beta(7, 3, 24) + 2,
    'area7': np.random.uniform(0, 4, 24),
    'area8': np.random.beta(3, 7, 24) * 2,
    'area9': np.random.normal(2, 1.4, 24),
    'area10': np.random.normal(1.3, 7, 24)
}

num_teams = 10
num_areas = 10
epsilon = 1.5
total_months = 24

resource_allocation = np.ones((total_months, num_areas)) * (num_teams // num_areas)
cumulative_value = np.zeros((total_months, num_areas))
data_points_collected = np.zeros((total_months, num_areas))

for month in range(total_months):
    if np.random.rand() < epsilon:
        area_to_explore = np.random.choice(num_areas)
        resource_allocation[month, area_to_explore] += 1
    else:
        area_to_exploit = np.argmax(cumulative_value[month-1])
        resource_allocation[month, area_to_exploit] += 1

    for area in range(num_areas):
        data_points_collected[month, area] += np.random.randint(1, 4) * resource_allocation[month, area]

    data_points_collected[month] *= resource_allocation[month]

    cumulative_value[month] = cumulative_value[month-1] + 0.5 * data_points_collected[month]
    epsilon *= 0.95

plt.figure(figsize=(12, 8))
plt.subplot(2, 1, 1)
for area in range(num_areas):
    plt.plot(range(total_months), resource_allocation[:, area], label=f'Area {area+1}')
plt.title('Resource Allocation Over Time')
plt.xlabel('Months')
plt.ylabel('Resource Allocation')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
for area in range(num_areas):
    plt.plot(range(total_months), cumulative_value[:, area], label=f'Area {area+1}')
plt.title('Cumulative Mineral Value Over Time')
plt.xlabel('Months')
plt.ylabel('Cumulative Value')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

estimated_values = {area: np.mean(values) for area, values in distributions.items()}
num_months = 24

for month in range(num_months):
    if np.random.rand() < epsilon:
        team_to_move = np.random.randint(num_teams)
        current_location = list(distributions.keys())[team_to_move]
        new_location = np.random.choice([area for area in distributions.keys() if area != current_location])

        print(f"Month {month + 1}: Team {team_to_move + 1} moved from {current_location} to {new_location}.")

    else:
        team_to_move = np.argmax([estimated_values[area] for area in distributions.keys()])
        new_location = list(distributions.keys())[team_to_move]

        print(f"Month {month + 1}: Team {team_to_move + 1} remained at {new_location}.")

    data_point = distributions[new_location][month]
    estimated_values[new_location] = (estimated_values[new_location] * (month + 1) + data_point) / (month + 2)

print("\nFinal estimates of mineral value for each area:")
for area, value in estimated_values.items():
    print(f"{area}: {value:.2f}")









#QUESTION 2.3
print("\n\nQUESTION 2.3 \n")

distributions = {
    'area1': np.random.beta(2, 2, 24) + 1,
    'area2': np.random.beta(3, 7, 24) * 3,
    'area3': np.random.normal(2.4, 1.8, 24),
    'area4': np.random.uniform(-1, 4, 24),
    'area5': np.random.normal(0, 9, 24),
    'area6': np.random.beta(7, 3, 24) + 2,
    'area7': np.random.uniform(0, 4, 24),
    'area8': np.random.beta(3, 7, 24) * 2,
    'area9': np.random.normal(2, 1.4, 24),
    'area10': np.random.normal(1.3, 7, 24)
}

num_teams = 10
num_areas = 10
epsilon = 0.5
total_months = 24
lock_duration = 6

resource_allocation = np.ones((total_months, num_areas)) * (num_teams // num_areas)
cumulative_value = np.zeros((total_months, num_areas))
data_points_collected = np.zeros((total_months, num_areas))

months_since_lock = 0

for month in range(total_months):
    if months_since_lock < lock_duration:
        months_since_lock += 1
    else:
        for _ in range(num_teams):
            if np.random.rand() < epsilon:
                area_to_explore = np.random.choice(num_areas)
                resource_allocation[month, area_to_explore] += 1
            else:
                area_to_exploit = np.argmax(cumulative_value[month-1])
                resource_allocation[month, area_to_exploit] += 1

    for area in range(num_areas):
        data_points_collected[month, area] += np.random.randint(1, 4) * resource_allocation[month, area]

    data_points_collected[month] *= resource_allocation[month]
    cumulative_value[month] = cumulative_value[month-1] + 0.5 * data_points_collected[month]
    epsilon *= 0.95

plt.figure(figsize=(12, 8))
plt.subplot(2, 1, 1)
for area in range(num_areas):
    plt.plot(range(total_months), resource_allocation[:, area], label=f'Area {area+1}')
plt.title('Resource Allocation Over Time')
plt.xlabel('Months')
plt.ylabel('Resource Allocation')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
for area in range(num_areas):
    plt.plot(range(total_months), cumulative_value[:, area], label=f'Area {area+1}')
plt.title('Cumulative Mineral Value Over Time')
plt.xlabel('Months')
plt.ylabel('Cumulative Value')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

estimated_values = {area: np.mean(values) for area, values in distributions.items()}

team_locks = {i: lock_duration for i in range(num_teams)}
months = np.arange(1, total_months + 1)

for month in range(total_months):
    for team in range(num_teams):
        if team_locks[team] > 0:
            team_locks[team] -= 1

    if month >= lock_duration:
        if np.random.rand() < epsilon:
            unlocked_teams = [team for team, lock in team_locks.items() if lock == 0]
            if unlocked_teams:
                team_to_move = np.random.choice(unlocked_teams)
                new_location = np.random.choice(list(distributions.keys()))
            else:
                continue
        else:
            unlocked_teams = [team for team, lock in team_locks.items() if lock == 0 and team != team_to_move]
            if unlocked_teams:
                team_to_move = max(unlocked_teams, key=lambda x: estimated_values[f'area{x + 1}'])
                available_areas = [area for area in distributions.keys() if area != f'area{team_to_move + 1}']
                new_location = np.random.choice(available_areas)
            else:
                continue

        print(f"Month {month+1}: Team {team_to_move+1} moved to {new_location}.")

        team_locks[team_to_move] = lock_duration
        data_point = distributions[new_location][month]
        estimated_values[new_location] = (estimated_values[new_location] * (month + 1) + data_point) / (month + 2)

print("\nFinal estimates of mineral value for each area:")
for area, value in estimated_values.items():
    print(f"{area}: {value:.2f}")













#QUESTION 3.1
print("\nQUESTION 3.1 \n")
aapl_data = pd.read_csv('AAPL.csv')[::-1]
tsla_data = pd.read_csv('TSLA.csv')[::-1]

aapl_data.columns = aapl_data.columns.str.strip()
tsla_data.columns = tsla_data.columns.str.strip()

aapl_data['Close'] = aapl_data['Close'].str.replace('$', '').astype(float)
aapl_data['Open'] = aapl_data['Open'].str.replace('$', '').astype(float)
aapl_data['High'] = aapl_data['High'].str.replace('$', '').astype(float)
aapl_data['Low'] = aapl_data['Low'].str.replace('$', '').astype(float)
tsla_data['Close'] = pd.to_numeric(tsla_data['Close'], errors='coerce')

aapl_data['High_Low_Diff'] = aapl_data['High'] - aapl_data['Low']
tsla_data['High_Low_Diff'] = tsla_data['High'] - tsla_data['Low']

aapl_data['Close_Change'] = aapl_data['Close'] - aapl_data['Close'].shift(1)
tsla_data['Close_Change'] = tsla_data['Close'] - tsla_data['Close'].shift(1)

plt.figure(figsize=(12, 6))
plt.plot(aapl_data['Date'], aapl_data['Close'], label='AAPL Close Price')
plt.plot(tsla_data['Date'], tsla_data['Close'], label='TSLA Close Price')
plt.title('AAPL and TSLA Close Price Over Time')
plt.xlabel('Date')
plt.ylabel('Close Price ($)')
plt.legend()
plt.grid(True)

x_ticks_positions = np.arange(0, len(aapl_data['Date']), step=63)
x_ticks_labels = aapl_data['Date'][::63]
plt.xticks(x_ticks_positions, x_ticks_labels, rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(aapl_data['High_Low_Diff'].dropna(), bins=20, alpha=0.5, label='AAPL')
plt.hist(tsla_data['High_Low_Diff'].dropna(), bins=20, alpha=0.5, label='TSLA')
plt.title('Distribution of High-Low Price Difference')
plt.xlabel('High-Low Difference ($)')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(aapl_data['Close_Change'].dropna(), bins=20, alpha=0.5, label='AAPL')
plt.hist(tsla_data['Close_Change'].dropna(), bins=20, alpha=0.5, label='TSLA')
plt.title('Distribution of Daily Close Price Change')
plt.xlabel('Close Price Change ($)')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()







#QUESTION 3.2
print("\n\nQUESTION 3.2 \n")

def generate_stock_paths(initial_price, drift, volatility, time_to_expiry, num_simulations, num_steps):
    dt = time_to_expiry / num_steps
    stock_paths = np.zeros((num_simulations, num_steps + 1))
    stock_paths[:, 0] = initial_price

    for i in range(num_simulations):
        for j in range(1, num_steps + 1):
            z = np.random.standard_normal(1)
            stock_paths[i, j] = stock_paths[i, j - 1] * np.exp(
                (drift - 0.5 * volatility ** 2) * dt + volatility * np.sqrt(dt) * z)

    return stock_paths

def calculate_drift(final_price, initial_price, time):
    return (np.log(final_price) - np.log(initial_price)) / time

def calculate_option_price(stock_paths, strike_price, time_to_expiry, risk_free_rate, volatility):
    discount_factor = np.exp(-risk_free_rate * time_to_expiry)
    call_payoffs = np.maximum(stock_paths[:, -1] - strike_price, 0)
    option_price = discount_factor * np.mean(call_payoffs)
    return option_price

volatility = 0.082  #8.2%
strike_price_aapl = 309.51
time_to_expiry = 1
num_simulations = 1000

drift_aapl = calculate_drift(strike_price_aapl, strike_price_aapl, time_to_expiry)
stock_paths_aapl = generate_stock_paths(strike_price_aapl, drift_aapl, volatility, time_to_expiry, num_simulations, 365)

risk_free_rate = 0.05
option_price_aapl = calculate_option_price(stock_paths_aapl, strike_price_aapl, time_to_expiry, risk_free_rate, volatility)

print("Simulated European Call option price for AAPL:", option_price_aapl)
plt.figure(figsize=(10, 6))
plt.plot(np.arange(366), stock_paths_aapl.T, linewidth=0.5)
plt.xlabel('Time (Days)')
plt.ylabel('Stock Price')
plt.title('Simulated Stock Price Paths for AAPL')
plt.show()

volatility_tsla = 0.082
strike_price_tsla = 650.57

drift_tsla = calculate_drift(strike_price_tsla, strike_price_tsla, time_to_expiry)
stock_paths_tsla = generate_stock_paths(strike_price_tsla, drift_tsla, volatility_tsla, time_to_expiry, num_simulations, 365)
option_price_tsla = calculate_option_price(stock_paths_tsla, strike_price_tsla, time_to_expiry, risk_free_rate, volatility_tsla)

print("Simulated European Call option price for TSLA:", option_price_tsla)
plt.figure(figsize=(10, 6))
plt.plot(np.arange(366), stock_paths_tsla.T, linewidth=0.5)
plt.xlabel('Time (Days)')
plt.ylabel('Stock Price')
plt.title('Simulated Stock Price Paths for TSLA')
plt.show()











#QUESTION 3.3
print("\n\nQUESTION 3.3 \n")

option_price_aapl_tsla = (option_price_aapl + option_price_tsla) / 2
print("Option price for AAPL+TESLA security before COVID slide:", option_price_aapl_tsla)

slide_down_percentage_aapl = 0.35
slide_down_percentage_tsla = 0.41
march_index = 60
num_days = 366
slide_down_index_aapl = int(march_index * slide_down_percentage_aapl)
slide_down_index_tsla = int(march_index * slide_down_percentage_tsla)

stock_paths_aapl[:, march_index:] -= stock_paths_aapl[:, march_index - 1].reshape(-1, 1) * slide_down_percentage_aapl
stock_paths_tsla[:, march_index:] -= stock_paths_tsla[:, march_index - 1].reshape(-1, 1) * slide_down_percentage_tsla

option_price_aapl_tsla_after_slide = calculate_option_price(
    (stock_paths_aapl + stock_paths_tsla) / 2,
    strike_price_aapl,
    time_to_expiry,
    risk_free_rate,
    (volatility + volatility_tsla) / 2
)
print("Option price for AAPL+TESLA security after COVID slide:", option_price_aapl_tsla_after_slide)

plt.figure(figsize=(10, 6))
for i in range(num_simulations):
    plt.plot(np.arange(num_days), (stock_paths_aapl[i] + stock_paths_tsla[i]) / 2, linewidth=0.5)
plt.xlabel('Time (Days)')
plt.ylabel('Stock Price')
plt.title('Simulated Stock Price Paths for AAPL+TESLA after COVID Slide')
plt.show()









#QUESTION 3.4(BONUS)
print("\n\nQUESTION 3.4(BONUS) \n")

num_simulations = 1000
num_days = 365
aapl_simulated_paths = np.zeros((num_simulations, num_days))
tsla_simulated_paths = np.zeros((num_simulations, num_days))

for i in range(num_simulations):
    aapl_simulated_paths[i] = generate_stock_paths(strike_price_aapl, drift_aapl, volatility, time_to_expiry, 1, num_days - 1)
    tsla_simulated_paths[i] = generate_stock_paths(strike_price_tsla, drift_tsla, volatility_tsla, time_to_expiry, 1, num_days - 1)

option_price_before_covid = calculate_option_price(
    (aapl_simulated_paths + tsla_simulated_paths) / 2,
    strike_price_aapl,
    time_to_expiry,
    risk_free_rate,
    (volatility + volatility_tsla) / 2
)

print("Option price for AAPL+TESLA security before mid-COVID growth:", option_price_before_covid)

growth_rate = 3
slump_percentage = 0.3
slump_month = 4
months_after_slump = 12 - slump_month + 1

mid_covid_growth_aapl = np.random.normal(0, volatility, (num_simulations, months_after_slump)) * growth_rate * (1 - slump_percentage) / months_after_slump
mid_covid_growth_tsla = np.random.normal(0, volatility_tsla, (num_simulations, months_after_slump)) * growth_rate * (1 - slump_percentage) / months_after_slump

for i in range(num_simulations):
    for j in range(months_after_slump):
        aapl_simulated_paths[i, slump_month + j:] *= np.exp(mid_covid_growth_aapl[i, j])
        tsla_simulated_paths[i, slump_month + j:] *= np.exp(mid_covid_growth_tsla[i, j])

option_price_after_covid = calculate_option_price(
    (aapl_simulated_paths + tsla_simulated_paths) / 2,
    strike_price_aapl,
    time_to_expiry,
    risk_free_rate,
    (volatility + volatility_tsla) / 2
)

print("Option price for AAPL+TESLA security after mid-COVID growth:", option_price_after_covid)

plt.figure(figsize=(10, 6))
for i in range(num_simulations):
    plt.plot(np.arange(num_days), (aapl_simulated_paths[i] + tsla_simulated_paths[i]) / 2, linewidth=0.5)
plt.xlabel('Time (Days)')
plt.ylabel('Stock Price')
plt.title('Simulated Stock Price Paths for AAPL+TESLA after Mid-COVID Growth')
plt.show()

















#QUESTION 4.1
print("\n\nQUESTION 4.1 \n")

insurance_data = pd.read_csv('insurance_data.csv')
total_charges = insurance_data['charges'].sum()
std_dev_charges = insurance_data['charges'].std()

expected_profit = 0.11 * total_charges
basic_insurance_rate = (total_charges + expected_profit) / len(insurance_data)
volatility = std_dev_charges / insurance_data['charges'].mean()

print("Basic Insurance Rate:", basic_insurance_rate)
print("Standard Deviation of Charges:", std_dev_charges)
print("Volatility:", volatility)








#QUESTION 4.2
print("\n\nQUESTION 4.2 \n")

age_categories = [(18, 22), (23, 30), (31, 48), (49, 130)]
total_charges_by_age = []
basic_insurance_rate_by_age = []

for age_range in age_categories:
    min_age, max_age = age_range
    age_group = insurance_data[(insurance_data['age'] >= min_age) & (insurance_data['age'] <= max_age)]
    total_charges = age_group['charges'].sum()
    total_charges_by_age.append(total_charges)
    basic_insurance_rate = total_charges * (1 + 0.11) / len(age_group)
    basic_insurance_rate_by_age.append(basic_insurance_rate)

std_dev_charges_by_age = [age_group['charges'].std() for age_group in [insurance_data[(insurance_data['age'] >= min_age) & (insurance_data['age'] <= max_age)] for min_age, max_age in age_categories]]
total_charges_sum = sum(total_charges_by_age)

volatility_by_age = [std_dev / age_group['charges'].mean() for std_dev, age_group in zip(std_dev_charges_by_age, [insurance_data[(insurance_data['age'] >= min_age) & (insurance_data['age'] <= max_age)] for min_age, max_age in age_categories])]

for i, age_range in enumerate(age_categories):
    print("Age Range:", age_range)
    print("Total Charges:", total_charges_by_age[i])
    print("Basic Insurance Rate:", basic_insurance_rate_by_age[i])
    print("Standard Deviation of Charges:", std_dev_charges_by_age[i])
    print("Volatility of Portfolio:", volatility_by_age[i])
    print()








#QUESTION 4.3
print("\n\nQUESTION 4.3 \n")

male_group = insurance_data[insurance_data['sex'] == 'male']
male_total_charges = male_group['charges'].sum()
male_total_people = len(male_group)
male_basic_insurance_rate = (male_total_charges / male_total_people) * 1.11
male_std_dev_charges = male_group['charges'].std()
male_volatility = male_std_dev_charges / male_group['charges'].mean()

female_group = insurance_data[insurance_data['sex'] == 'female']
female_total_charges = female_group['charges'].sum()
female_total_people = len(female_group)
female_basic_insurance_rate = (female_total_charges / female_total_people) * 1.11
female_std_dev_charges = female_group['charges'].std()
female_volatility = female_std_dev_charges / female_group['charges'].mean()

print("ALL MALES:")
print(f"Total Charges: {male_total_charges}\nBasic Insurance Rate: {male_basic_insurance_rate}\nStd Dev Charges: {male_std_dev_charges}\nVolatility: {male_volatility}\n")

print("ALL FEMALES:")
print(f"Total Charges: {female_total_charges}\nBasic Insurance Rate: {female_basic_insurance_rate}\nStd Dev Charges: {female_std_dev_charges}\nVolatility: {female_volatility}\n")

age_categories = [(18, 22), (23, 30), (31, 48), (49, 130)]
sex_categories = ['male', 'female']
insurance_info_by_age_sex = []

for age_range in age_categories:
    min_age, max_age = age_range
    for sex in sex_categories:
        age_sex_group = insurance_data[(insurance_data['age'] >= min_age) & (insurance_data['age'] <= max_age) & (insurance_data['sex'] == sex)]
        total_charges = age_sex_group['charges'].sum()
        total_people = len(age_sex_group)
        basic_insurance_rate = (total_charges / total_people) * 1.11
        std_dev_charges = age_sex_group['charges'].std()
        volatility = std_dev_charges / age_sex_group['charges'].mean()
        insurance_info_by_age_sex.append((age_range, sex, total_charges, basic_insurance_rate, std_dev_charges, volatility))

for entry in insurance_info_by_age_sex:
    age_range, sex, total_charges, basic_insurance_rate, std_dev_charges, volatility = entry
    print(f"Gender and Age Range: {sex} - {age_range}\nTotal Charges: {total_charges}\nBasic Insurance Rate: {basic_insurance_rate}\nStd Dev Charges: {std_dev_charges}\nVolatility: {volatility}\n")







#QUESTION 4.4
print("\n\nQUESTION 4.4 \n")

known_claimants_data = insurance_data[insurance_data['charges'] > 0]
total_charges_known_claimants = known_claimants_data['charges'].sum()
num_known_claimants = len(known_claimants_data)
annual_rate_claimants = total_charges_known_claimants / num_known_claimants

print("Annual Rate on the Claimants:", annual_rate_claimants)