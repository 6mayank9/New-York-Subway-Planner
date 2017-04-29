# New-York-Subway-Planner
Project to optimize the subway routes using real-time MTA feeds for Algorithms course in Rutgers University.

The User has three options to select from <br />
  1. Crowdedness: When the user wants to travel on a route with less crowd <br />
 2: Time: When user wants to travel in minimum time <br />
 3: Transfers: When user wants to travel without changing many lines <br />
<br />
Not all subway lines are considered due to lack of data. For time feature we have considered Lines 1-6 and for other two features we have Lines 1-6,N,Q,R,W,B,D. Once we have the data for the other lines we can easily extend our project to cover them as well.<br />

You can find the graph of the subway in SubwayGraph folder. We used python library networkx to build a graph using the unique station codes provided by MTA. We also have a dictionary to get additional information about a station ID. The graph and dictionary is stored as a pkl file and can be imported to anyfile when required.<br />

I'll update soon the methods used to calculate the weights for each feature. <br />

Using this weighted graph we calculate the shortest distance using Dijkstra's algorithm. Which is then plotted on a map using folium.
  
  
 Thanks to MTA for providing real time feeds and turnstiledata.

# How to run: 
Download the files to your local server.
Run Final.html
