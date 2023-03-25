import requests
import json
response = requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=2232e923")
print(response)
