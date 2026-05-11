import requests
import json
import pandas as pd

def main():
    # a real public API - no key needed
    url = "https://api.open-meteo.com/v1/forecast"
    
    # query parameters — like query() in httr
    params = {
        "latitude":   36.6,
        "longitude": -121.9,
        "hourly":    "temperature_2m,precipitation",
        "forecast_days": 3
    }

    # make the GET request
    response = requests.get(url, params=params)

    # check it worked — 200 means success, like status_code in httr
    print(f"status code: {response.status_code}")

    # always check status before using data
    if response.status_code == 200:
        print("request successful")
    elif response.status_code == 401:
        print("authentication error - check your API key")
    elif response.status_code == 404:
        print("endpoint not found")
    else:
        print(f"unexpected status: {response.status_code}")

    # raise an exception automatically if something went wrong
    # like stop() in R but automatic
    response.raise_for_status()

       # parse the JSON response
    data = response.json()

    # look at the top level keys — like names() in R
    print(f"top level keys: {list(data.keys())}")

    # dig into the hourly data
    hourly = data["hourly"]
    print(f"hourly keys: {list(hourly.keys())}")

    # convert to dataframe
    df = pd.DataFrame({
        "time":        hourly["time"],
        "temp_c":      hourly["temperature_2m"],
        "precip_mm":   hourly["precipitation"]
    })

    print(df.head(10))
    print()

    # save raw response to JSON file for inspection
    with open("api_response.json", "w") as f:
        json.dump(data, f, indent=2)
    print("saved raw response to api_response.json")

    # adding headers — like add_headers() in httr
    # most real APIs need this for authentication
    headers = {
        "Authorization": "Bearer YOUR_TOKEN_HERE",
        "Content-Type":  "application/json"
    }
    # you'd pass this as: requests.get(url, headers=headers, params=params)

    # POST request — like POST() in httr
    # used when sending data to an API
    payload = {"site_id": 42, "start_date": "2024-01-01"}
    # response = requests.post(url, json=payload, headers=headers)

if __name__ == "__main__":
    main()