import pandas as pd
import requests
import json

def main():
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude":   49.2,
        "longitude": -125.9,
        "hourly":    "temperature_2m,precipitation,wind_speed_10m",
        "forecast_days": 4
    }

    response = requests.get(url, params=params)

    print(f"status code: {response.status_code}")

    if response.status_code == 200:
        print("request successful")
    elif response.status_code == 401:
        print("authentication error - check your API key")
    elif response.status_code == 404:
        print("endpoint not found")
    else:
        print(f"unexpected status: {response.status_code}")

    response.raise_for_status()

    # get data
    data = response.json()
    hourly = data["hourly"]

    # dataframe
    df = pd.DataFrame({
        "time": hourly["time"],
        "temp_c": hourly["temperature_2m"],
        "wind": hourly["wind_speed_10m"],
        "precip": hourly["precipitation"]
    })
    
    summary = df.agg({"temp_c": ["mean", "max"]})
    print(summary)

    summary_clean = df[["temp_c", "wind", "precip"]].agg(["mean", "max"])
    print(summary_clean)


    with open("api_response.json", "w") as f:
        json.dump(data, f, indent=2)
    print("saved raw response to api_response.json")
    


if __name__ == "__main__":
    main()



