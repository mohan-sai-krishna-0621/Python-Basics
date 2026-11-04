
import requests


def get_coordinates(city):
    """Find the latitude and longitude of a city."""

    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    if "results" not in data or not data["results"]:
        print("City not found!")
        return None

    location = data["results"][0]

    return {
        "name": location["name"],
        "country": location.get("country", "Unknown"),
        "latitude": location["latitude"],
        "longitude": location["longitude"]
    }


def get_weather(latitude, longitude):
    """Fetch current weather information."""

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": (
            "temperature_2m,"
            "relative_humidity_2m,"
            "apparent_temperature,"
            "wind_speed_10m,"
            "weather_code"
        )
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    return response.json()


def describe_weather(code):
    """Convert weather codes into readable descriptions."""

    weather_conditions = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Slight snow",
        73: "Moderate snow",
        75: "Heavy snow",
        80: "Slight rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        95: "Thunderstorm"
    }

    return weather_conditions.get(code, "Unknown conditions")


def display_weather(location, weather):
    """Display weather information."""

    current = weather["current"]

    print("\n========== WEATHER REPORT ==========")
    print(f"City: {location['name']}")
    print(f"Country: {location['country']}")

    print(f"Temperature: {current['temperature_2m']} °C")
    print(f"Feels Like: {current['apparent_temperature']} °C")
    print(f"Humidity: {current['relative_humidity_2m']}%")
    print(f"Wind Speed: {current['wind_speed_10m']} km/h")

    condition = describe_weather(current["weather_code"])
    print(f"Weather: {condition}")

    print("====================================")


def main():
    print("===== WEATHER DATA VIEWER =====")

    while True:
        city = input("\nEnter city name (or type exit): ").strip()

        if city.lower() == "exit":
            print("Thank you for using Weather Data Viewer!")
            break

        if not city:
            print("City name cannot be empty!")
            continue

        try:
            location = get_coordinates(city)

            if location is None:
                continue

            weather = get_weather(
                location["latitude"],
                location["longitude"]
            )

            display_weather(location, weather)

        except requests.exceptions.Timeout:
            print("Request timed out. Please try again.")

        except requests.exceptions.ConnectionError:
            print("Internet connection problem!")

        except requests.exceptions.HTTPError as error:
            print("API returned an HTTP error:", error)

        except requests.exceptions.RequestException as error:
            print("Request failed:", error)

        except (KeyError, TypeError, ValueError):
            print("Unexpected weather data received from the API.")


if __name__ == "__main__":
    main()
