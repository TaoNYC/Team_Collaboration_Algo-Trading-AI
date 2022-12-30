import os
import requests

"""
This Python file stores API keys as environment variables using the os.env dictionary.
The keys can then be accessed and used in API requests using the requests library.
"""

# Set environment variables for API keys
os.env['API_KEY_1'] = 'abc123'  # key for endpoint 1
os.env['API_KEY_2'] = 'def456'  # key for endpoint 2
os.env['API_KEY_3'] = 'ghi789'  # key for endpoint 3
os.env['API_KEY_4'] = 'jkl101'  # key for endpoint 4
os.env['API_KEY_5'] = 'mno102'  # key for endpoint 5
os.env['API_KEY_6'] = 'pqr103'  # key for endpoint 6
os.env['API_KEY_7'] = 'stu104'  # key for endpoint 7
os.env['API_KEY_8'] = 'vwx105'  # key for endpoint 8
os.env['API_KEY_9'] = 'yz106'   # key for endpoint 9
os.env['API_KEY_10'] = 'abc107' # key for endpoint 10

# Access API keys using os.env
api_key_1 = os.env['API_KEY_1']
api_key_2 = os.env['API_KEY_2']
api_key_3 = os.env['API_KEY_3']
api_key_4 = os.env['API_KEY_4']
api_key_5 = os.env['API_KEY_5']
api_key_6 = os.env['API_KEY_6']
api_key_7 = os.env['API_KEY_7']
api_key_8 = os.env['API_KEY_8']
api_key_9 = os.env['API_KEY_9']
api_key_10 = os.env['API_KEY_10']


"""
The HTTP methods GET, POST, and PUT are used to send requests to a server to retrieve, create, or update resources. 

These methods are part of the HTTP protocol, which is used to communicate between web servers and clients (such as web browsers).

The GET method is used to retrieve a resource from the server. It is the most common HTTP method, and is typically used to retrieve data from a server or API.

The POST method is used to create a new resource on the server. It is often used to submit data to a server, such as when filling out a form on a website or creating a new record in a database.

The PUT method is used to update an existing resource on the server. It is often used to update data on a server or API, such as when editing an existing record in a database.

In the example code provided, 
the GET method is used to retrieve data from an API endpoint, 
the POST method is used to submit data to an API endpoint, and 
the PUT method is used to update data on an API endpoint. 
The specific details of how these methods are used will depend on the API and the resources it exposes.

"""
# Use API keys in API requests
response = requests.get(f'https://api.example.com/endpoint1?key={api_key_1}')

data = response.json()

response = requests.post(f'https://api.example.com/endpoint2?key={api_key_2}', json=data)

response = requests.put(f'https://api.example.com/endpoint3?key={api_key_3}', json=data)

response = requests.post(f'https://api.example.com/endpoint4?key={api_key_4}', json=data)

response = requests.put(f'https://api.example.com/endpoint5?key={api_key_5}', json=data)

response = requests.post(f'https://api.example.com/endpoint6?key={api_key_6}', json=data)

response = requests.put(f'https://api.example.com/endpoint7?key={api_key_7}', json=data)

response = requests.post(f'https://api.example.com/endpoint8?key={api_key_8}', json=data)

response = requests.put(f'https://api.example.com/endpoint9?key={api_key_9}', json=data)

response = requests.post(f'https://api.example.com/endpoint10?key={api_key_10}', json=data)

