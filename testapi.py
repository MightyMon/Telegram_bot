import requests
import json
response = requests.get("http://www.omdbapi.com/?<api-key>")
print(response)
