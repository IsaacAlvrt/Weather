# data.py 
# GETS THE USER'S LOCATION AND WEATHER

from geopy.geocoders import Nominatim
import geocoder
import requests

# GET LATITUDE AND LONGITUDE
g = geocoder.ip('me')
latlng = g.latlng

lat = latlng[0]
lon = latlng[1]

# GET CITY
geolocator = Nominatim(user_agent="geoapiExercises")
location = geolocator.reverse(f'{lat},{lon}')

address = location.raw['address']
city = address['city']

# GET WEATHER FROM RapidAPI
url = "https://community-open-weather-map.p.rapidapi.com/find"

querystring = {
    "q": city, 
    "units":"metric"
    }

headers = {
    'x-rapidapi-key': "dc0c7bf93cmsh677e885936c4596p117065jsnc7cc0f3f16c0",
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# DATA
data = response.json()['list'][0]

"""
    # Weather in metric system
    
    weather = data['main']['temp']
    feels_like = data['main']['feels_like']
    max = data['main']['temp_max']
    min = data['main']['temp_min']
    city = data['name']
    description = data['weather'][0]['description']
    icon = data['weather'][0]['icon']
"""