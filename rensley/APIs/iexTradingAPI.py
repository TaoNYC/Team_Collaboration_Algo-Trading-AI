import requests

# Set the API endpoint and the stock symbol
endpoint = "https://api.iextrading.com/1.0/stock/{symbol}/quote"
symbol = "AAPL"

# Send a request to the API endpoint
response = requests.get(endpoint.format(symbol=symbol))

# Check the status code of the response
if response.status_code != 200:
    raise Exception("Failed to retrieve stock prices")

# Extract the stock data from the response
stock_data = response.json()

# Print the stock data
print(f"Stock symbol: {stock_data['symbol']}")
print(f"Stock price: {stock_data['latestPrice']}")
