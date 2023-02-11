import pandas as pd
import numpy as np
import sqlite3
import secrets 
import requests 


# Open a connection to the database file
conn = sqlite3.connect('top_10_bots.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table to store the top ten bots
cursor.execute('''CREATE TABLE IF NOT EXISTS top_10_bots
                (id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT,
                algorithm TEXT NOT NULL,
                score FLOAT NOT NULL);''')

# Insert the top ten bots into the table
top_10_bots = [
    {'name': 'Bot 1', 'description': 'This bot is awesome!', 'algorithm': 'Q-learning', 'score': 0.85},
    {'name': 'Bot 2', 'description': 'This bot is great!', 'algorithm': 'SARSA', 'score': 0.75},
    {'name': 'Bot 3', 'description': 'This bot is good!', 'algorithm': 'Deep Q-Network', 'score': 0.65},
    {'name': 'Bot 4', 'description': 'This bot is okay!', 'algorithm': 'Monte Carlo', 'score': 0.55},
    {'name': 'Bot 5', 'description': 'This bot is meh!', 'algorithm': 'Temporal Difference', 'score': 0.45},
    {'name': 'Bot 6', 'description': 'This bot is bad!', 'algorithm': 'Actor-Critic', 'score': 0.35},
    {'name': 'Bot 7', 'description': 'This bot is terrible!', 'algorithm': 'Policy Gradient', 'score': 0.25},
    {'name': 'Bot 8', 'description': 'This bot is awful!', 'algorithm': 'Genetic Algorithms', 'score': 0.15},
    {'name': 'Bot 9', 'description': 'This bot is horrendous!', 'algorithm': 'Evolution Strategies', 'score': 0.05},
    {'name': 'Bot 10', 'description': 'This bot is the worst!', 'algorithm': 'Random Search', 'score': 0.01}
]

for i, bot in enumerate(top_10_bots):
    cursor.execute("INSERT INTO top_10_bots (id, name, description, algorithm, score) VALUES (?, ?, ?, ?, ?)", (i+1, bot['name'], bot['description'], bot['algorithm'], bot['score']))

# Commit the changes and close the connection to the database
conn.commit()
conn.close()




def update_top_10_bots(new_bot):
    # Connect to the database
    conn = sqlite3.connect('top_10_bots.db')
    c = conn.cursor()

    # Check if new bot's score is higher than any of the existing bots' scores
    c.execute('SELECT * FROM top_10_bots ORDER BY score DESC LIMIT 10')
    current_top_bots = c.fetchall()
    if len(current_top_bots) < 10 or new_bot['score'] > current_top_bots[-1][4]:
        # Add new bot to table and remove lowest scoring bot
        c.execute("INSERT INTO top_10_bots (name, description, algorithm, score) VALUES (?, ?, ?, ?)",
                  (new_bot['name'], new_bot['description'], new_bot['algorithm'], new_bot['score']))
        c.execute('SELECT * FROM top_10_bots ORDER BY score DESC LIMIT 10')
        current_top_bots = c.fetchall()
        if len(current_top_bots) > 10:
            c.execute('DELETE FROM top_10_bots WHERE id=?', (current_top_bots[-1][0],))

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Example usage
new_bot = {'name': 'Bot 11', 'description': 'This bot is incredible!', 'algorithm': 'Deep Reinforcement Learning', 'score': 0.9}
update_top_10_bots(new_bot)




# Read the CSV file into a pandas dataframe
df = pd.read_csv('top_10_bots.csv')

# Print the dataframe to verify the data has been read correctly
print(df.head())



# Read the CSV file into a pandas dataframe
df = pd.read_csv('top_10_bots.csv')

# Print the dataframe to verify the data has been read correctly
print(df.head())


# Write the updated top ten bots to the CSV file
df.to_csv('top_10_bots.csv', index=False)