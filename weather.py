import requests
import json

api_key = "5687930061604b11aea175002261304"
api_url = "https://api.weatherapi.com/v1/current.json"

zip_codes = ["90045", "10001", "60601", "77001", "85001"]
rows = []

for zip_code in zip_codes:
    params = {"key": api_key, "q": zip_code}
    response = requests.get(api_url, params=params)
    data = response.json()

    rows.append({
        "zip": zip_code,
        "location": data["location"]["name"],
        "temp_f": data["current"]["temp_f"],
        "condition": data["current"]["condition"]["text"],
        "humidity": data["current"]["humidity"]
    })

print(rows)

import pandas as pd

df = pd.DataFrame(rows)
df.to_csv("weather_data.csv", index=False)
print(df)