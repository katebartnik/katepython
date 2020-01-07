# pobieranie kursow walut via JSON z api.nbp.pl

import requests
import json

url = "http://api.nbp.pl/api/exchangerates/tables/A?format=json"
r = requests.get(url)
#print(r.text)
json_data = json.loads(r.text)
#print(type(json_data[0]))
nbp_data = json_data[0]
print(nbp_data.keys())
print(f"Tablica {nbp_data.get('table')}")
print(f"Numer {nbp_data.get('no')}")
print(f"Data {nbp_data.get('effectiveDate')}")

rates = nbp_data.get("rates")
for rate in rates:
    print("-"*60)
    print(f"{rate.get('currency')}\t\t\t{rate.get('code')}\t{rate.get('mid')}")