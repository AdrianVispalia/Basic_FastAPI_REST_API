'''API test file'''
#!/usr/bin/python3

import requests


# Get country data
API1_URL = "https://restcountries.com/v3.1/all?fields=name,population"
response = requests.get(API1_URL, timeout=10).json()
data = [
    {
        "name": country["name"]["official"],
        "population": country["population"]
    } for country in response
]
print("Obtained data")


# Create DB
API2_URL = "http://localhost:8000/api/v1"
print(requests.get(API2_URL + "/create", timeout=10).content)


# Post country data
headers = {'Content-Type': "application/json", 'Accept': "application/json"}
for country in data:
    requests.post(API2_URL + "/data/countries", json=country, headers=headers, timeout=5)


# Get countries
countries = requests.get(API2_URL + "/data/countries", timeout=10).json()
print(countries)
assert len(countries) > 0


# Get country
country = requests.get(API2_URL + "/data/countries/Kingdom%20of%20Spain", timeout=10).json()
print(country)
assert country == { "name": "Kingdom of Spain", "population": 47351567 }


# Get nonexistent country
nonexistent_country_request = requests.get(API2_URL + "/data/countries/Spain", timeout=10)
assert nonexistent_country_request.status_code == 404


# Create duplicate country
duplicate_country = { "name": "Kingdom of Spain", "population": 47351567 }
duplicate_country_request = requests.post(API2_URL + "/data/countries", json=duplicate_country, \
                                            headers=headers, timeout=10)
assert duplicate_country_request.status_code == 409
