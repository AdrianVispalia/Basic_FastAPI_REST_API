#!/usr/bin/python3

import requests

# Get country data
API1_URL = "https://restcountries.com/v3.1/all?fields=name,population"
response = requests.get(API1_URL).json()
data = [
    {
        "name": country["name"]["official"],
        "population": country["population"]
    } for country in response
]


# Create DB
API2_URL = "http://localhost:8000/api/v1/"
print(requests.get(API2_URL + "create").content)


# Post country data
headers = {'Content-Type': "application/json", 'Accept': "application/json"}
for country in data:
    requests.post(API2_URL + "/data/coountries", json=country, headers=headers)


# Get countries
print(requests.get(API2_URL + "/data/countries").json())
