import pandas as pd
import folium
from pandas import compat
 
 
subways = pd.read_csv("subway_stops.csv")
 
nyc = folium.Map(location=[subways.stop_lat.mean(axis=0),subways.stop_lon.mean(axis=0)], zoom_start=12)

for each in subways.iterrows():  
    folium.CircleMarker(list([each[1]['stop_lat'],each[1]['stop_lon']]),radius=7, popup=each[1]['stop_name'], color='#3186cc',
                    fill_color='#3186cc').add_to(nyc)
 
nyc.save("subway.html")
