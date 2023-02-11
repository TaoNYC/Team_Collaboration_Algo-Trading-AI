import numpy as np
import matplotlib.pyplot as plt

NUM_TRIALS = 100
EPS = 0.1
ALPHA = 0.1
GAMMA = 0.9
NUM_STATES = 10
NUM_ACTIONS = 2

class Environment:
    def __init__(self):
        self.state = 0

    def reset(self):
        self.state = 0

    def get_reward(self, action):
        if action == 1:
            self.state += 1
        if self.state == NUM_STATES - 1:
            return 1
        else:
            return 0

class QLearningAgent:
    def __init__(self):
        self.Q = np.zeros((NUM_STATES, NUM_ACTIONS))

    def select_action(self, state, eps):
        if np.random.random() < eps:
            return np.random.choice(NUM_ACTIONS)
        else:
            return np.argmax(self.Q[state, :])

    def update(self, state, action, reward, next_state):
        self.Q[state, action] += ALPHA * (reward + GAMMA * np.max(self.Q[next_state, :]) - self.Q[state, action])

def experiment():
    env = Environment()
    agent = QLearningAgent()

    rewards = np.zeros(NUM_TRIALS)
    optimal = np.zeros(NUM_TRIALS+1)

    print("Running simulation...")
    for i in range(NUM_TRIALS):
        env.reset()
        done = False
        total_reward = 0
        while not done:
            state = env.state
            action = agent.select_action(state, EPS)
            reward = env.get_reward(action)
            next_state = env.state
            agent.update(state, action, reward, next_state)
            total_reward += reward
            if env.state == NUM_STATES - 1:
                done = True

        rewards[i] = total_reward
        optimal[i] = 1 if np.argmax(agent.Q[i, :]) == 1 else 0

    print("\nSimulation complete.\n")
    print("Q values:")
    print(agent.Q)
    print("Total reward earned:", rewards.sum())
    print("Overall win rate:", rewards.sum() / NUM_TRIALS)
    print("Optimal action rate:", optimal.sum() / NUM_TRIALS)

    cumulative_rewards = np.cumsum(rewards)
    win_rates = cumulative_rewards / (np.arange(NUM_TRIALS) + 1)
    plt.plot(win_rates)
    plt.plot(np.ones(NUM_TRIALS))
    plt.legend(['win rate', 'optimal rate'])
    plt.show()

if __name__ == "__main__":
    experiment()
