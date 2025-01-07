import numpy as np
import matplotlib.pyplot as plt

#PART 1
def get_probabilities(drift=0):
    probs = [
        np.random.normal(0, 5),
        np.random.normal(-0.5, 12),
        np.random.normal(2, 3.9),
        np.random.normal(-0.5, 7),
        np.random.normal(-1.2, 8),
        np.random.normal(-3, 7),
        np.random.normal(-10, 20),
        np.random.normal(-0.5, 1),
        np.random.normal(-1, 2),
        np.random.normal(1, 6),
        np.random.normal(0.7, 4),
        np.random.normal(-6, 11),
        np.random.normal(-7, 1),
        np.random.normal(-0.5, 2),
        np.random.normal(-6.5, 1),
        np.random.normal(-3, 6),
        np.random.normal(0, 8),
        np.random.normal(2, 3.9),
        np.random.normal(-9, 12),
        np.random.normal(-1, 6),
        np.random.normal(-4.5, 8)
    ]

    return probs


def choose_action(actions, epsilon):
    num_actions = len(actions)
    p = np.random.random()
    if p < epsilon:
        j = np.random.choice(num_actions)
    else:
        j = np.argmax([a['runningMean'] for a in actions])
    x = np.random.randn() + actions[j]['mean']
    actions[j]['numTimesChosen'] += 1
    actions[j]['runningMean'] = (1 - 1.0 / actions[j]['numTimesChosen']) * actions[j]['runningMean'] + 1.0 / actions[j]['numTimesChosen'] * x

    return x


def run_epsilon_greedy(epsilon, numOfSteps, probabilities, num_simulations):
    cumulative_averages = np.zeros(numOfSteps)

    for _ in range(num_simulations):
        actions = [{'mean': probabilities[i], 'runningMean': 0, 'numTimesChosen': 0} for i in range(len(probabilities))]
        data = np.empty(numOfSteps)

        for i in range(numOfSteps):
            x = choose_action(actions, epsilon)
            data[i] = x

        cumulative_averages += np.cumsum(data) / (np.arange(numOfSteps) + 1)

    return cumulative_averages / num_simulations


def run_thompson_sampling(numOfSteps, probabilities, num_simulations):
    cumulative_averages = np.zeros(numOfSteps)

    for _ in range(num_simulations):
        actions = [{'mean': probabilities[i], 'runningMean': 0, 'numTimesChosen': 0} for i in range(len(probabilities))]
        data = np.empty(numOfSteps)

        for i in range(numOfSteps):
            samples = [np.random.normal(a['runningMean'], 1.0 / np.sqrt(a['numTimesChosen']) if a['numTimesChosen'] > 0 else 1.0) for a in actions]
            j = np.argmax(samples)
            x = np.random.randn() + actions[j]['mean']
            actions[j]['numTimesChosen'] += 1
            actions[j]['runningMean'] = (1 - 1.0 / actions[j]['numTimesChosen']) * actions[j]['runningMean'] + 1.0 / actions[j]['numTimesChosen'] * x

            data[i] = x

        cumulative_averages += np.cumsum(data) / (np.arange(numOfSteps) + 1)

    return cumulative_averages / num_simulations

def find_optimal_epsilon(epsilon_values, numOfSteps, probabilities, num_simulations):
    optimal_epsilon = None
    best_convergence_speed = float()

    for epsilon in epsilon_values:
        result = run_epsilon_greedy(epsilon, numOfSteps, probabilities, num_simulations)
        convergence_speed = result[-1]

        if convergence_speed > best_convergence_speed:
            best_convergence_speed = convergence_speed
            optimal_epsilon = epsilon

    return optimal_epsilon


if __name__ == '__main__':
    probabilities = get_probabilities()

    epsilons = [0.01, 0.05, 0.1, 0.4]
    num_simulations = 1

    optimal_epsilon = find_optimal_epsilon(epsilons, 10000, probabilities, num_simulations)

    print(f"Optimal Epsilon for Best Convergence Speed: {optimal_epsilon}")

    # Run epsilon greedy
    for epsilon in epsilons:
        result = run_epsilon_greedy(epsilon, 10000, probabilities, num_simulations)
        plt.plot(result, label=f'Epsilon-Greedy (eps={epsilon})')

    #Run Thompson Sampling
    thompson_result = run_thompson_sampling(10000, probabilities, num_simulations)
    plt.plot(thompson_result, label='Thompson Sampling')

    plt.legend()
    plt.xlabel('Time Steps')
    plt.ylabel('Average Reward')
    plt.title('Epsilon-Greedy vs Thompson Sampling')
    plt.show()










#PART 2
def get_probabilities_for_part_2(time_step, drift=0.001):
    if time_step >= 3000:
        mean_shifts = [7, 0, 3, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0]
    else:
        mean_shifts = [0] * 20

    total_drift = drift * time_step

    probs = [
        np.random.normal(0 - total_drift + mean_shifts[0], 5),
        np.random.normal(-0.5 - total_drift + mean_shifts[1], 12),
        np.random.normal(2 - total_drift + mean_shifts[2], 3.9),
        np.random.normal(-0.5 - total_drift + mean_shifts[3], 7),
        np.random.normal(-1.2 - total_drift + mean_shifts[4], 8),
        np.random.normal(-3 - total_drift + mean_shifts[5], 7),
        np.random.normal(-10 - total_drift + mean_shifts[6], 20),
        np.random.normal(-0.5 - total_drift + mean_shifts[7], 1),
        np.random.normal(-1 - total_drift + mean_shifts[8], 2),
        np.random.normal(1 - total_drift + mean_shifts[9], 6),
        np.random.normal(0.7 - total_drift + mean_shifts[10], 4),
        np.random.normal(-6 - total_drift + mean_shifts[11], 11),
        np.random.normal(-7 - total_drift + mean_shifts[12], 1),
        np.random.normal(-0.5 - total_drift + mean_shifts[13], 2),
        np.random.normal(-6.5 - total_drift + mean_shifts[14], 1),
        np.random.normal(-3 - total_drift + mean_shifts[15], 6),
        np.random.normal(0 - total_drift + mean_shifts[16], 8),
        np.random.normal(2 - total_drift + mean_shifts[17], 3.9),
        np.random.normal(-9 - total_drift + mean_shifts[18], 12),
        np.random.normal(-1 - total_drift + mean_shifts[19], 6)
    ]

    if probs[7] - mean_shifts[7] > 3 * 3:
        probs[7] = 50

    return probs

def choose_action(actions, epsilon):
    if np.random.random() < epsilon:
        return np.random.randint(len(actions))
    else:
        return np.argmax([a['mean'] for a in actions])

def update_action(action, x):
    action['numTimesChosen'] += 1
    action['mean'] = (1 / action['numTimesChosen']) * action['mean'] / action['numTimesChosen'] * x

def run_epsilon_greedy(epsilon, numOfSteps, num_simulations):
    cumulative_averages = np.zeros(numOfSteps)

    for _ in range(num_simulations):
        data = np.empty(numOfSteps)
        actions = [{'mean': 0, 'numTimesChosen': 0} for _ in range(20)]

        for i in range(numOfSteps):
            probabilities = get_probabilities_for_part_2(i)
            j = choose_action(actions, epsilon)
            x = np.random.randn() + probabilities[j]
            update_action(actions[j], x)
            data[i] = x

        cumulative_averages += np.cumsum(data) / (np.arange(numOfSteps) + 1)

    return cumulative_averages / num_simulations

def run_thompson_sampling(numOfSteps, num_simulations):
    cumulative_averages = np.zeros(numOfSteps)

    for _ in range(num_simulations):
        data = np.empty(numOfSteps)
        actions = [{'mean': 0, 'numTimesChosen': 0} for _ in range(20)]

        for i in range(numOfSteps):
            probabilities = get_probabilities_for_part_2(i)
            samples = [np.random.normal(a['mean'], 1.0 / np.sqrt(a['numTimesChosen']) if a['numTimesChosen'] > 0 else 1.0) for a in actions]
            j = np.argmax(samples)
            x = np.random.randn() + probabilities[j]
            update_action(actions[j], x)
            data[i] = x

        cumulative_averages += np.cumsum(data) / (np.arange(numOfSteps) + 1)

    return cumulative_averages / num_simulations


def run_thompson_sampling_with_restart(numOfSteps, num_simulations, restart_time=3000):
    cumulative_averages = np.zeros(numOfSteps)

    for _ in range(num_simulations):
        data = np.empty(numOfSteps)
        actions = [{'mean': 0, 'numTimesChosen': 0} for _ in range(20)]

        for i in range(numOfSteps):
            if i == restart_time:
                # Reset everything at restart time t=3000
                actions = [{'mean': 0, 'numTimesChosen': 0} for _ in range(20)]

            probabilities = get_probabilities_for_part_2(i)
            samples = [np.random.normal(a['mean'], 1.0 / np.sqrt(a['numTimesChosen']) if a['numTimesChosen'] > 0 else 1.0) for a in actions]
            j = np.argmax(samples)
            x = np.random.randn() + probabilities[j]
            update_action(actions[j], x)
            data[i] = x

        cumulative_averages += np.cumsum(data) / (np.arange(numOfSteps) + 1)

    return cumulative_averages / num_simulations

if __name__ == '__main__':
    epsilons = [0.01, 0.05, 0.1, 0.4]
    num_simulations = 1

    convergence_rates = []

    #Run epsilon greedy
    for epsilon in epsilons:
        result = run_epsilon_greedy(epsilon, 10000, num_simulations)
        plt.plot(result, label=f'Epsilon-Greedy (eps={epsilon})')

        final_steps = int(0.1 * len(result))
        convergence_rate = np.mean(result[-final_steps:])
        convergence_rates.append(convergence_rate)

    #Run Thompson Sampling
    thompson_result = run_thompson_sampling(10000, num_simulations)
    plt.plot(thompson_result, label='Thompson Sampling')

    #Run Thompson Sampling with restart at t=3000
    thompson_result_restart = run_thompson_sampling_with_restart(10000, num_simulations, restart_time=3000)
    plt.plot(thompson_result_restart, label='Thompson Sampling with Restart at t=3000')

    plt.legend()
    plt.xlabel('Time Steps')
    plt.ylabel('Average Reward')
    plt.title('Epsilon-Greedy vs Thompson Sampling')
    plt.show()

    optimal_epsilon = epsilons[np.argmax(convergence_rates)]
    print(f'Optimal Epsilon for Best Convergence Speed: {optimal_epsilon}')