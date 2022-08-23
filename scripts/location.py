from geopy.geocoders import Nominatim
from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

geolocator = Nominatim(user_agent="coordinateconverter")

address = '42.2817131, -83.7465425'

location = geolocator.reverse(address)
print(location)