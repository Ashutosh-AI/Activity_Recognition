import json
from urllib.request import urlopen
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def location():
    url = "https://ipinfo.io/json"
    response = urlopen(url)
    data = json.load(response)
    #print(data)

    locations = "The Location is, IP: {}, Address is {} {} {} and Latitude and Longitude are ({}) and Postal Code is {}"\
                .format(data["ip"], data["city"], data["region"], data["country"], data["loc"], data["postal"])

    return locations


"""import geopy.geocoders as geocoder
import geopy
import socket

# Get the IP address of your laptop.
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print("Your laptop's IP address is:", ip_address)

# Create a Nominatim geocoder object.
geolocator = geocoder.Nominatim(user_agent="my_app")

# Use the geocoder object to get the location of the IP address.
location = geolocator.geocode(ip_address)

# Print the latitude and longitude of the location.
print(location.latitude, location.longitude)"""
