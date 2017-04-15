import pandas as pd
import folium
from pandas import compat
import pickle
import networkx as nx

class station:                                # station class to store attributes of each subway station
    def __init__(self, stop_id, stop_name, trains, latitude, longitude):
        self.id = stop_id                     # Unique Station ID
        self.name = stop_name                 # Station name
        self.trains = trains                  # List of trains at this staion
        self.longitude = longitude
        self.latitude = latitude

import turnstiledata

subways = pd.read_csv("subway_stops.csv")
 
nyc = folium.Map(location=[subways.stop_lat.mean(axis=0),subways.stop_lon.mean(axis=0)], zoom_start=12)

for each in subways.iterrows():  
    folium.CircleMarker(list([each[1]['stop_lat'],each[1]['stop_lon']]),radius=7, popup=each[1]['stop_name'], color='#3186cc',
                    fill_color='#3186cc').add_to(nyc)
 
nyc.save("subway.html")

filehandler = open("alldumps.pkl","rb")
subwayDictionary,G = pickle.load(filehandler)
path = turnstiledata.getPath("1011","2012")
for i in path:
    print subwayDictionary[i].name