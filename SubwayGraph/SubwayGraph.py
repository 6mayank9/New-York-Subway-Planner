'''This file converts the csv into a networkx undirected graph
'''
import csv
import networkx as nx
import matplotlib.pyplot as plt
class station:                                # station class to store attributes of each subway station
    def __init__(self, stop_id, stop_name, trains):
        self.id = stop_id                     # Unique Station ID
        self.name = stop_name                 # Station name
        self.trains = trains                  # List of trains at this staion
check = 201
G = nx.Graph()                                # Undirected graph
stations = []
subwayDictionary = {}                         # Dictionary to get station object from station id
b = station("a", "a", "a")
with open('SubwayStops1.csv') as csvfile:
    readCsv = csv.reader(csvfile, delimiter=',')
    readCsv.next()
    for row in readCsv:
        if(str(row[0]) in subwayDictionary):
            a = subwayDictionary[str(row[0])]
        else:
            a = station(row[0],row[1],row[5])
            subwayDictionary[str(row[0])] = a
        if(a.id!=str(check)):
            G.add_edge(a, b)                  # Add weight of edges here if required or later when reading gpickle file
        else:
            check+=100
        stations.append(a)
        b = a
import pickle
newfile = open("alldumps.pkl","wb")           # Dumps the graph and dictionary to a file
pickle.dump([subwayDictionary,G],newfile)

'''Get Neighbors from station id'''
k = G.neighbors(subwayDictionary["224"])
print subwayDictionary["224"].name+" number of neighbors are ",len(k)
for i in range(len(k)):
    print k[i].name

#print nx.info(G)
nx.draw(G)
#print nx.is_connected(G)
D = list(nx.connected_component_subgraphs(G)) # Get the list of connected components
#for i in range(len(D[20])):
#    print D[20].nodes()[i].id

#print nx.info(D[0])
#plt.show()