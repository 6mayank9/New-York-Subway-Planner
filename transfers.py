import pickle
import networkx as nx

class station:                                # station class to store attributes of each subway station
    def __init__(self, stop_id, stop_name, trains, latitude, longitude):
        self.id = stop_id                     # Unique Station ID
        self.name = stop_name                 # Station name
        self.trains = trains                  # List of trains at this staion
        self.longitude = longitude
        self.latitude = latitude
filehandler = open("allTransfersDumps.pkl","rb")
subwayDictionary,G = pickle.load(filehandler)

def getPath(source,destination):
    route = nx.dijkstra_path(G, source, destination, 'weight')
    length = nx.dijkstra_path_length(G, source, destination, 'weight')
    return route, length

