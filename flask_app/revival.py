# IMPORTS

# import descartes
import folium
# import geopandas as gpd
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# import pdfplumber
import requests
import time

from bs4 import BeautifulSoup
from flask import Flask, render_template
from folium.plugins import MarkerCluster
from IPython.display import HTML, Video

%matplotlib inline
# %xmode Minimal
# %xmode Plain
# %xmode Context
%xmode Verbose 
# Verbose exception mode: This is for me for testing; feel free to turn it off!

# FUNCTIONS

# This function uses the GeoJS API to identify or approximate 
# a user's location NOTE: This is based on IP address, which
# reduces accuracy

def identify_user_location():
    
    get_ip = requests.get('https://get.geojs.io/v1/ip.json') # request user's IP address
    ip_address = get_ip.json()['ip']                         # parse via json
    location_request = requests.get('https://get.geojs.io/v1/ip/geo/' + ip_address + '.json') 
    # request additional params
    location_parameters = location_request.json()            # parse via json 
    user_longitude = location_parameters['longitude']
    user_latitude = location_parameters['latitude']
    return (user_longitude, user_latitude)

# This function uses the GeoCoder.ca API to get a pair of 
# lat/long coordinates by looking up the postal code

def postal_code_to_lat_long(postcode):
    location_request = requests.get('https://geocoder.ca/?postal=' + postcode + '&geoit=XML&json=1')
    location_parameters = location_request.json()
    latitude = location_parameters['latt']
    longitude = location_parameters['longt']
    return latitude, longitude

# The Haversine formula is a mathematical equation for finding the distance 
# between two points on the globe given that it is spherical and not flat.
# The original author of this implementation is Wayne Dyck. I edited it to better suit
# my objectives.


def distance(origin_lat, origin_long, dest_lat, dest_long):

    earths_radius = 6371 # km

    dlat = math.radians(dest_lat - origin_lat)
    dlon = math.radians(dest_long - origin_long)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(origin_lat)) \
        * math.cos(math.radians(dest_lat)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = earths_radius * c

    return d


# This simple function takes a pandas series representing the contents 
# of a dataframe column, and isolates the first value. It strips out some 
# extraneous values that are part of the series.

def isolate_the_variable(pandas_series):
    return pandas_series.tolist()[0]

# MAIN BODY

user_name = input('Welcome to the Naloxone pharmacy locator. May I please have your first name? ')

user_location = identify_user_location()
user_longitude = user_location[0]
user_latitude = user_location[1]
    
# Set up a dataframe with their information
user_details = {'Name': [user_name],
            'Address': ['Current User Location'],
            'City': ['Current city'],
            'Postcode': ["Current location postal code"],
            'Latitude': [user_latitude],
            'Longitude': [user_longitude]}
    
user_data = pd.DataFrame(user_details)

# Read in the pharmacies list and append the user's information to that dataframe
pharmacy_locator = pd.read_csv('csv/toronto_pharmacies_final.csv', dtype = {'Longitude' : 'float64', 'Latitude' : 'float64'})
pharmacy_locator = pharmacy_locator.append(user_data)

# Convert to a geopandas geodataframe
# pharmacy_locator = gpd.GeoDataFrame(pharmacy_locator, geometry=gpd.points_from_xy(pharmacy_locator.Longitude, pharmacy_locator.Latitude))

# Ensure that all the lat/long data is datatype float not str 
pharmacy_locator = pharmacy_locator.astype({'Longitude' : 'float', 'Latitude' : 'float'})

# Sort by location using pandas built-in sort_values function, 
# default algorithm is quicksort (average time commplexity is θ(n log(n))) 
pharmacy_locator.sort_values(['Longitude', 'Latitude'], ascending=[False, False], inplace=True)
pharmacy_locator.reset_index(drop=True, inplace=True)

# Now that the list (including the user's location) is sorted by location,
# identify the two closest locations, which should be directly above and below it
user_index = pharmacy_locator[pharmacy_locator['Name']==user_name].index.values
user_observation = pharmacy_locator.loc[user_index]
user_latitude = user_observation['Latitude'].tolist()[0] 
user_longitude = user_observation['Longitude'].tolist()[0]
user_coordinates = user_latitude, user_longitude

previous_observation = pharmacy_locator.loc[user_index - 1]
subsequent_observation = pharmacy_locator.loc[user_index + 1]

# Create distance-from-user column
pharmacy_locator.insert(6, 'Distance', 0.0)

# Assign to variables the long and lat of the user's location and the
# two locations closest to it. 

origin_lat = isolate_the_variable(user_observation['Latitude'])
origin_long = isolate_the_variable(user_observation['Longitude'])

previous_lat = isolate_the_variable(previous_observation['Latitude'])
previous_long = isolate_the_variable(previous_observation['Longitude'])

subsequent_lat = isolate_the_variable(subsequent_observation['Latitude'])
subsequent_long = isolate_the_variable(subsequent_observation['Longitude'])

previous_distance = distance(origin_lat, origin_long, previous_lat, previous_long)
subsequent_distance = distance(origin_lat, origin_long, subsequent_lat, subsequent_long)

if previous_distance >= subsequent_distance:
    closest_pharmacy = previous_observation
else:
    closest_pharmacy = subsequent_observation

closest_pharmacy_latitude = isolate_the_variable(closest_pharmacy['Latitude']) 
closest_pharmacy_longitude = isolate_the_variable(closest_pharmacy['Longitude'])
closest_pharmacy_coordinates = closest_pharmacy_latitude, closest_pharmacy_longitude
    
closest_PN = closest_pharmacy['Name']
closest_pharmacy_name = isolate_the_variable(closest_PN)

closest_PA = closest_pharmacy['Address']
closest_pharmacy_address = isolate_the_variable(closest_PA)

closest_PLat = closest_pharmacy['Latitude']
closest_pharmacy_latitude = isolate_the_variable(closest_PLat)

closest_PLong = closest_pharmacy['Longitude']
closest_pharmacy_latitude = isolate_the_variable(closest_PLong)

print('Identifying your location, ' + user_name + '. Your closest pharmacy is ' + closest_pharmacy_name + ', located at ' + closest_pharmacy_address + '.')

print('Here is a map showing your nearest pharmacy, ' + user_name + '.')

#Create the map
pharmacy_map = folium.Map(location = user_coordinates, zoom_start = 13)
                         
folium.Marker(user_coordinates, popup = 'You are here').add_to(pharmacy_map)
folium.Marker(closest_pharmacy_coordinates, popup = closest_pharmacy_name).add_to(pharmacy_map)

#Display the map
pharmacy_map