import requests


def get_weather() -> None:
    api_key = "f89358b2221f41f8a6c130205251109"
    if not api_key:
        raise ValueError()

    url = "http://api.weatherapi.com/v1/current.json"
    params = {"key": api_key, "q": "Paris", "aqi": "no"}

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    city = data["location"]["name"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"Weather in {city}: {temp_c}°C, {condition}")


if __name__ == "__main__":
    get_weather()
