import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import beta

NUM_TRIALS = 10000
EPS = 0.1
BANDIT_PROBABILITIES = [0.2, 0.5, 0.75]

class Bandit:
    def __init__(self, p):
        self.p = p
        self.p_estimate = 0
        self.N = 0

    def pull(self):
        return np.random.random() < self.p

    def update(self, x):
        self.N += 1
        self.p_estimate = ((self.N - 1) * self.p_estimate + x) / self.N

    def get_upper_bound(self, t):
        return beta.ppf(0.95, self.N * self.p_estimate + 1, self.N * (1 - self.p_estimate) + 1)

def experiment():
    bandits = [Bandit(p) for p in BANDIT_PROBABILITIES]

    rewards = np.zeros(NUM_TRIALS)
    num_times_explored = 0
    num_times_exploited = 0
    num_optimal = 0
    optimal_j = np.argmax([b.p for b in bandits])

    print("Running simulation...")
    for i in range(NUM_TRIALS):
        if np.random.random() < EPS:
            num_times_explored += 1
            j = np.random.randint(len(BANDIT_PROBABILITIES))
        else:
            num_times_exploited += 1
            j = np.argmax([b.get_upper_bound(i+1) for b in bandits])

        if j == optimal_j:
            num_optimal += 1

        x = bandits[j].pull()
        rewards[i] = x
        bandits[j].update(x)

    print("\nSimulation complete.\n")
    print("Bandit win probabilities:", BANDIT_PROBABILITIES)
    print("Bandit estimates:")
    for i, b in enumerate(bandits):
        ci_low = beta.ppf(0.025, b.N * b.p_estimate + 1, b.N * (1 - b.p_estimate) + 1)
        ci_high = beta.ppf(0.975, b.N * b.p_estimate + 1, b.N * (1 - b.p_estimate) + 1)
        print(f"Bandit {i+1}: {b.p_estimate:.4f} ({ci_low:.4f}, {ci_high:.4f})")
    print("Total reward earned:", rewards.sum())
    print("Overall win rate:", rewards.sum() / NUM_TRIALS)
    print("Number of times explored:", num_times_explored)
    print("Number of times exploited:", num_times_exploited)
    print("Number of times selected optimal bandit:", num_optimal)

    cumulative_rewards = np.cumsum(rewards)
    win_rates = cumulative_rewards / (np.arange(NUM_TRIALS) + 1)
    plt.plot(win_rates)
    plt.plot(np.ones(NUM_TRIALS)*np.max(BANDIT_PROBABILITIES))
    for b in bandits:
        upper_bound = [b.get_upper_bound(t) for t in range(1, NUM_TRIALS+1)]
        plt.plot(upper_bound, '--')
    plt.legend(['win rate', 'optimal rate', 'bandit 1', 'bandit 2', 'bandit 3'])
    plt.show()

if __name__ == "__main__":
    experiment()
