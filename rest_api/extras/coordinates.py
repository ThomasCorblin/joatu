import requests
import urllib.parse
from decimal import Decimal
from math import pi, acos, cos, sin
from hubs.models import HubGeolocation




def coordinates_calculation(street, postal_code, city, country):
    API_key = 'AIzaSyDM17QITeync0gIHsGgyqG_IxLH-7JSHo0'
    main_api = "https://maps.googleapis.com/maps/api/geocode/json?"
    address = street + ' ' + postal_code + ' ' + city + ' ' + country
    url = main_api + urllib.parse.urlencode({'address':address})+ '&key='+API_key
    json_data = requests.get(url).json()
    lat= Decimal(json_data['results'][0]['geometry']['location']['lat'])
    lng= Decimal(json_data['results'][0]['geometry']['location']['lng'])
    return lat, lng



def offer__demand_coordinates_calculation(number, street, postal_code, city):
    API_key = 'AIzaSyDM17QITeync0gIHsGgyqG_IxLH-7JSHo0'
    main_api = "https://maps.googleapis.com/maps/api/geocode/json?"
    address =number+' ' +street + ' ' + postal_code + ' ' + city 
    url = main_api + urllib.parse.urlencode({'address':address})+ '&key='+API_key
    json_data = requests.get(url).json()
    lat= Decimal(json_data['results'][0]['geometry']['location']['lat'])
    lng= Decimal(json_data['results'][0]['geometry']['location']['lng'])
    return lat, lng


