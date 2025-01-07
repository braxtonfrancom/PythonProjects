import matplotlib.pyplot as plt
plt.style.use('Solarize_Light2')
import pandas as pd
import csv
import random


#PART 1:
def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = [row[0] for row in reader if row]
    return data

def optimal_stopping_analysis(data, len_candidates=100, num_experiments=10000):
    solution_found_count = {}
    optimal_solution_found_count = {}

    for i in range(1, len_candidates):
        solution_found_count[str(i)] = 0
        optimal_solution_found_count[str(i)] = 0

    for experiment in range(num_experiments):
        candidates = random.sample(data, len_candidates)
        optimal_candidate = max(candidates)

        for i in range(1, len_candidates):
            max_before_i = max(candidates[0:i])
            for candidate in candidates[i:-1]:
                if candidate > max_before_i:
                    solution_found_count[str(i)] += 1
                    if candidate == optimal_candidate:
                        optimal_solution_found_count[str(i)] += 1
                    break

    x_percentage = [int(i) * 100 / len_candidates for i in solution_found_count.keys()]
    y = list(optimal_solution_found_count.values())

    return x_percentage, y

def plot_optimal_stopping(x, y, csv_name):
    plt.xlabel("Optimal Stopping Percent")
    plt.ylabel("Number of times optimal solution is found (out of 10000)")
    plt.title(f"Optimal Stopping Analysis - {csv_name}")
    plt.plot(x, y)
    plt.show()


scenario1_data = read_csv('scenario1-1.csv')
x1, y1 = optimal_stopping_analysis(scenario1_data)
plot_optimal_stopping(x1, y1, 'scenario1-1.csv')


scenario2_data = read_csv('scenario2.csv')
x2, y2 = optimal_stopping_analysis(scenario2_data)
plot_optimal_stopping(x2, y2, 'scenario2.csv')



#Histogram to analyze distribution of scenario2.csv
df = pd.read_csv('scenario2.csv', header=None)

numbers = df[0]

plt.hist(numbers, bins=100, color='blue', edgecolor='black', alpha=0.7)
plt.xlabel('Number')
plt.ylabel('Frequency')
plt.title('Distribution of Numbers in scenario2.csv')
plt.show()




###########################################################################################################



#PART 2
def gen_uniform_data(size):
    return [min(99, random.uniform(1, 99)) for _ in range(size)]

def gen_normal_data(size, mean=50, std_dev=10):
    return [min(99, max(1, int(random.normalvariate(mean, std_dev)))) for _ in range(size)]

def max_benefit_stopping_analysis(data, len_candidates=100, num_experiments=1000):
    avg_reward = {}
    for i in range(1, len_candidates):
        total_reward = 0
        for experiment in range(num_experiments):
            candidates = random.sample(data, len_candidates)
            threshold = max(candidates[:i])
            reward = threshold - i
            total_reward += reward
        avg_reward[str(i)] = total_reward / num_experiments

    x, y = zip(*avg_reward.items())
    return x, y

def plot_max_benefit_stopping(x, y, dis_type):
    plt.xlabel("Threshold Percent")
    plt.ylabel("Average Reward")
    plt.title(f"Max Benefit Stopping Analysis - {dis_type}")
    plt.plot(x, y)
    plt.show()

#Uniform Distribution
uniform_data = gen_uniform_data(1000)
x_uniform, y_uniform = max_benefit_stopping_analysis(uniform_data)
plot_max_benefit_stopping(x_uniform, y_uniform, 'Uniform Distribution')

#Normal Distribution
normal_data = gen_normal_data(1000)
x_normal, y_normal = max_benefit_stopping_analysis(normal_data)
plot_max_benefit_stopping(x_normal, y_normal, 'Normal Distribution')