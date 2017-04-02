'''This file converts the csv into a networkx undirected graph
'''
import csv
import networkx as nx
import matplotlib.pyplot as plt
import simplejson as json
from networkx.readwrite import json_graph



def adj_list_to_file(B,file_name):
    f = open('Adjacency_List.txt', "w")
    for n in B.nodes():
        f.write(n + ' ')
        for neighbor in B.neighbors(n):
            f.write(neighbor + ' ')
        f.write('\n')
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
'''Lines 1-6 & S Graph '''
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
            G.add_edge(a.id, b.id, weight=1)                  # Add weight of edges here if required or later when reading gpickle file
        else:
            if check == 601:
                check = 901
            else:
                check += 100

        b = a
G.remove_node("a")
'''Lines B,D,N,Q,R,W graph'''
for i in ["B","D","N","Q","R","W"]:
    with open('Line'+i+'.csv') as file:
        readCsv = csv.reader(file, delimiter=',')
        temp = readCsv.next()
        c = station(temp[0],temp[1],temp[5])
        subwayDictionary[str(temp[0])] = c
        for row in readCsv:
            if(str(row[0]) in subwayDictionary):
                d = subwayDictionary[str(row[0])]
            else:
                d = station(str(row[0]),row[1],row[5])

                subwayDictionary[str(row[0])] = d
                stations.append(a)
            G.add_edge(d.id,c.id, weight =1)
            c=d
'''Connecting Same Station with multiple ids'''
G.add_edge("901","631",weight = 0)  #Grand Central
G.add_edge("127","902",weight = 0)  #Times Sq
G.add_edge("R16","901",weight = 0)  #Times Sq
G.add_edge("R17","D17",weight = 0)  #Herald Sq
G.add_edge("R20","635",weight = 0)  #14 St - Union Sq
G.add_edge("R23","Q01",weight = 0)  #Canal St
G.add_edge("639","R01",weight = 0)  #Canal St
G.add_edge("235","D24",weight = 0)  #Atlantic Av-Barclays
G.add_edge("R31","235",weight = 0)  #Atlantic Av-Barclays
G.add_edge("A24","125",weight = 0)  #58 St - Columbus Circle


import pickle
newfile = open("alldumps.pkl","wb")           # Dumps the graph and dictionary to a file
pickle.dump([subwayDictionary,G],newfile)

'''Get Neighbors from station id
k = G.neighbors(subwayDictionary["101"])
print subwayDictionary["101"].name+" number of neighbors are ",len(k)
for i in range(len(k)):
    print k[i].name+" "+k[i].id
'''
#print nx.info(G)
nx.draw(G)
#print nx.is_connected(G)
D = list(nx.connected_component_subgraphs(G)) # Get the list of connected components
print "Total connected components are: ",len(D)
print subwayDictionary["Q05"].name
#for i in range(len(D[0])):
#    print D[0].nodes()[i].id
#adj_list_to_file(G,"tst.txt")

jsondump = json_graph.node_link_data(G)
jsondump['links'] = [{
            'source': jsondump['nodes'][link['source']]['id'],
            'target': jsondump['nodes'][link['target']]['id']
        }
        for link in jsondump['links']]

with open('networkdata1.json', 'w') as outfile1:
    outfile1.write(json.dumps(jsondump))
#print nx.info(D[0])
#plt.show()