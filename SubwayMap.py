#!/Python27/python
import pandas as pd
import folium
from pandas import compat
import pickle
import networkx as nx
import sys
import cgi

class station:                                # station class to store attributes of each subway station
    def __init__(self, stop_id, stop_name, trains, latitude, longitude):
        self.id = stop_id                     # Unique Station ID
        self.name = stop_name                 # Station name
        self.trains = trains                  # List of trains at this staion
        self.longitude = longitude
        self.latitude = latitude



form = cgi.FieldStorage()
criteria =  form.getvalue('min')
start =  form.getvalue('origin')
end =  form.getvalue('dest')

if criteria == "Crowd":
    import turnstiledata
elif criteria == "Time":
    import realtime_data
else:
    import transfers
subways = pd.read_csv("subway_stops.csv")
 
nyc = folium.Map(location=[subways.stop_lat.mean(axis=0),subways.stop_lon.mean(axis=0)], zoom_start=12)

for each in subways.iterrows():  
    folium.CircleMarker(list([each[1]['stop_lat'],each[1]['stop_lon']]),radius=7, popup=each[1]['stop_name'], color='#3186cc',
                    fill_color='#3186cc').add_to(nyc)
 
nyc.save("subway.html")

filehandler = open("alldumps.pkl","rb")
subwayDictionary,G = pickle.load(filehandler)
import csv
def stop_name_to_stopid(x):
    stopidset=[]
    with open('SubwayStops.csv') as stopname:
        reader = csv.DictReader(stopname)
        for row in reader:
            if row['stop_name'] == x:
                stopidset.append(str(row['stop_id'])+str(row['trains'][0:1]))                
    return stopidset

source = stop_name_to_stopid(start)
destination = stop_name_to_stopid(end)
temp = sys.maxint
finalpath=[]
for a in range(len(source)):
    for b in range(len(destination)):
        try:
            if criteria == "Crowd":
                path, length = turnstiledata.getPath(source[a],destination[b])
            elif criteria == "Time":
                path, length = realtime_data.getPath(source[a],destination[b])
            else:
                path, length = transfers.getPath(source[a],destination[b])
            if(length<temp):
                finalpath = path
                temp = length
        except:
            continue


if len(finalpath) == 0:
    print "Content-type: text/html"
    print
    print "<html>"
    print "<head>"
    print "<title>Error</title>"
    print "</head>"
    print "<body>"
    print "<p>Path Not Found</p>"
    print "</body>"
    print "</html>"
else:
    minpath = []
    for key in finalpath:
        minpath.append(tuple([subwayDictionary[key].latitude, subwayDictionary[key].longitude]))

    folium.PolyLine(minpath, color="red", weight=2.5, opacity=1).add_to(nyc)

    nyc.save("subway.html")

    print "Content-type: text/html"
    print
    f = open("subway.html", "r")
    for row in f:
        print row
