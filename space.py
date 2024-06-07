import os
import requests
import streamlit as st
from geopy.geocoders import Nominatim
#from dotenv import load_dotenv

#load env variable
#load_dotenv()

#load streamlit env variable

def get_coordinates (loc):
    #making an instance of Nominatim class
    geolocator = Nominatim(user_agent="geo_request")
    
    #applying geocode method to get the location
    location = geolocator.geocode(loc)

    #return address,lat,long
    return location.address,location.latitude,location.longitude

def get_satellites(lat, lng):
    #api_key = os.getenv("API_KEY")
    #api_secret = os.getenv("API_SECRET")
    api_key = st.secrets["API_KEY"]
    api_secret = st.secrets["API_SECRET"]
    url = f'https://api.n2yo.com/rest/v1/satellite/above/{lat}/{lng}/0/10/0&apiKey={api_secret}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch satellite data")
