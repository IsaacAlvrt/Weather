# EXTERNAL LIBRARIES
from flask import Flask, render_template
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


# START FLASK APP
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)