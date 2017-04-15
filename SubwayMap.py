import pandas as pd
import folium
from pandas import compat
import pickle
import networkx as nx
import cgi

class station:                                # station class to store attributes of each subway station
    def __init__(self, stop_id, stop_name, trains, latitude, longitude):
        self.id = stop_id                     # Unique Station ID
        self.name = stop_name                 # Station name
        self.trains = trains                  # List of trains at this staion
        self.longitude = longitude
        self.latitude = latitude

import turnstiledata

form = cgi.FieldStorage()
criteria =  form.getvalue('min')
start =  form.getvalue('origin')
end =  form.getvalue('dest')

subways = pd.read_csv("subway_stops.csv")
 
nyc = folium.Map(location=[subways.stop_lat.mean(axis=0),subways.stop_lon.mean(axis=0)], zoom_start=12)

for each in subways.iterrows():  
    folium.CircleMarker(list([each[1]['stop_lat'],each[1]['stop_lon']]),radius=7, popup=each[1]['stop_name'], color='#3186cc',
                    fill_color='#3186cc').add_to(nyc)
 
nyc.save("subway.html")

filehandler = open("alldumps.pkl","rb")
subwayDictionary,G = pickle.load(filehandler)
path = turnstiledata.getPath("1011","2012")
import csv
def stop_name_to_stopid(x):
    stopidset=[]
    with open('SubwayStops.csv') as stopname:
        reader = csv.DictReader(stopname)
        for row in reader:
            if row['stop_name'] == x:
                stopidset.append(str(row['stop_id'])+str(row['trains'][0:1]))                
    return stopidset
print stop_name_to_stopid('96 St')
source = stop_name_to_stopid(start)
destination = stop_name_to_stopid(end)
temp = sys.maxint

for a in range(len(source)):
    for b in range(len(destination)):
        path, length = turnstiledata(source[a],destination[b])
        if(length<temp):
            finalpath = path
            temp = length


for i in finalpath:
    print subwayDictionary[i].name
 
minpath=[]
for key in subwayDictionary:
    minpath.append(tuple(subwayDictionary[key]))
    
folium.PolyLine(minpath, color="red", weight=2.5, opacity=1).add_to(nyc)
 
nyc.save("subway.html")
