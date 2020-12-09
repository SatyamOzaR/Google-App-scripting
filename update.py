import requests

# defining our sheet name in the 'id' variable and the the column where we want to update the value
parameters = {"id":"Sheet1", "value":15} 

URL = "<--Your Webapp URL-->"

response = requests.get(URL, params=parameters)

print(response.content)
