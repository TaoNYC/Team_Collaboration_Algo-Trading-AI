
import numpy as np

# Define the environment
class Environment:
    def __init__(self):
        # Initialize the state and end states
        self.state = 0
        self.end_states = [3, 6]
        
        # Define the possible actions
        self.actions = [0, 1, 2]
    
    # Get the current state
    def get_state(self):
        return self.state
    
    # Check if the current state is an end state
    def is_end(self):
        return self.state in self.end_states
    
    # Get the possible actions for the current state
    def get_actions(self):
        return self.actions
    
    # Take a given action and update the state
    def take_action(self, action):
        # Move one state ahead if action 0 is taken
        if action == 0:
            self.state += 1
        # Move two states ahead if action 1 is taken
        elif action == 1:
            self.state += 2
        # Move three states ahead if action 2 is taken
        elif action == 2:
            self.state += 3

# Define the Q-learning algorithm
class QLearning:
    def __init__(self, env, alpha=0.1, gamma=0.9):
        # Initialize the environment and the Q-table
        self.env = env
        self.q_table = np.zeros((7, 3))
        
        # Set the learning rate (alpha) and discount factor (gamma)
        self.alpha = alpha
        self.gamma = gamma
    
    # Learn from a single episode
    def learn(self):
        # Get the current state and actions
        state = self.env.get_state()
        actions = self.env.get_actions()
        
        # Choose an action using an epsilon-greedy policy
        epsilon = 0.1
        if np.random.uniform(0, 1) < epsilon:
            # Choose a random action with probability epsilon
            action = np.random.choice(actions)
        else:
            # Choose the action with the highest estimated reward
            action = np.argmax(self.q_table[state])
        
        # Take the action and get the reward
        self.env.take_action(action)
        reward = 1 if self.env.is_end() else 0
        
        # Update the Q-table using the Q-learning update rule
        next_state = self.env.get_state()
        self.q_table[state][action] += self.alpha * (reward + self.gamma * np.max(self.q_table[next_state]) - self.q_table[state][action])

# Create the environment and the Q-learning algorithm
env = Environment()
q_learning = QLearning(env)

# Train the AI bot through a series of episodes
for episode in range(1000):
    # Reset the environment to the starting state
    env.state = 0
    
    # Run the episode until the end state is reached
    while not env.is_end():
        q_learning.learn()

# Print the final Q-table
print(q_learning.q_table)
