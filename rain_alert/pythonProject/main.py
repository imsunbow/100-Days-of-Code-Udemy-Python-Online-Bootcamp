import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "da1f68839ae277ddf418d63477d44304"

weather_params = {
    "lat": 37.568291,
    "lon": 126.997780,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(OWM_Endpoint,params=weather_params)
weather_data = response.json()
print(weather_data)