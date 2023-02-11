import requests
import pandas as pd
import sqlite3

headers = {'User-Agent': 'ranly196@gmail.com'}

# SEC indexes companies by a 10-digit Central Index Key (CIK)
tickers_cik = requests.get("https://www.sec.gov/files/company_tickers.json", headers=headers)

# Save the response to a JSON file
with open('companies_tickers.json', 'w') as f:
    f.write(tickers_cik.text)

# Load the data from the JSON file into a Pandas DataFrame
companies_tickers = pd.read_json('companies_tickers.json')

# Connect to SQLite database
conn = sqlite3.connect('sec_filings.db')

# Save the DataFrame to the database
companies_tickers.to_sql('companies_tickers', conn, if_exists='replace')

# Close the database connection
conn.close()
