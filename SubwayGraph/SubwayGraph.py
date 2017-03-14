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
b = station("a", "dummyStation", "-A")
'''Lines 1-6 Graph'''
with open('Lines1-6.csv') as csvfile:
    readCsv = csv.reader(csvfile, delimiter=',')
    readCsv.next()
    for row in readCsv:
        if(str(row[0]) in subwayDictionary):
            a = subwayDictionary[str(row[0])]
        else:
            a = station(row[0],row[1],row[5])
            subwayDictionary[str(row[0])] = a
            stations.append(a)
        if(a.id!=str(check)):
            G.add_edge(a, b)                  # Add weight of edges here if required or later when reading gpickle file
        else:
            check+=100

        b = a
'''Lines A-F graph'''
for i in ["A","B","C","D","E","F"]:
    with open('Line'+i+'.csv') as file:
        readCsv = csv.reader(file, delimiter=',')
        temp = readCsv.next()
        c = station(temp[0],temp[1],temp[5])
        for row in readCsv:
            if(str(row[0]) in subwayDictionary):
                d = subwayDictionary[str(row[0])]
            else:
                d = station(row[0],row[1],row[5])
                subwayDictionary[str(row[0])] = d
                stations.append(a)
            G.add_edge(d,c)
            c=d

import pickle
newfile = open("alldumps.pkl","wb")           # Dumps the graph and dictionary to a file
pickle.dump([subwayDictionary,G],newfile)

'''Get Neighbors from station id'''
k = G.neighbors(subwayDictionary["101"])
print subwayDictionary["101"].name+" number of neighbors are ",len(k)
for i in range(len(k)):
    print k[i].name+" "+k[i].id

#print nx.info(G)
nx.draw(G)
#print nx.is_connected(G)
D = list(nx.connected_component_subgraphs(G)) # Get the list of connected components
print "Total connected components are: ",len(D)
for i in range(len(D[0])):
    print D[0].nodes()[i].id

#print nx.info(D[0])
#plt.show()