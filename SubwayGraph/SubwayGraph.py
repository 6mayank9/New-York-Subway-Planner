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
    def __init__(self, stop_id, stop_name, trains, latitude, longitude):
        self.id = stop_id                     # Unique Station ID
        self.name = stop_name                 # Station name
        self.trains = trains                  # List of trains at this staion
        self.longitude = longitude
        self.latitude = latitude
check = 201
G = nx.Graph()                                # Undirected graph
stations = []
subwayDictionary = {}                         # Dictionary to get station object from station id
line = str(1)
check = ["201","301","401","501","601","901",""]
p=0
b = station("a", "dummyStation", "-A", 0, 0)
'''Lines 1-6 & S Graph '''
with open('Lines1-6.csv') as csvfile:
    readCsv = csv.reader(csvfile, delimiter=',')
    readCsv.next()
    for row in readCsv:
        row[0] = str(str(row[0])+line)
        #print row[0]
        a = station(row[0],row[1],row[5], row[2], row[3])
        subwayDictionary[str(row[0])] = a
        stations.append(a)
        for h in ["1","2","3","4","5","6"]:
            if (str(str(row[0][:3])+h) in subwayDictionary) and (str(str(row[0][:3])+h) != str(row[0])):
                connect = subwayDictionary[str(str(row[0][:3])+h)]
                #print "Connecting: ",a.id," ",connect.id
                G.add_edge(a.id,connect.id, weight = 0)
        if(a.id[:3]!=str(check[p])):
            G.add_edge(a.id, b.id, weight=1)                  # Add weight of edges here if required or later when reading gpickle file
        else:

            p += 1
            print str(row[0])
            subwayDictionary.pop(str(row[0]))                 # remove station with wrong line ID

            line = str(int(line)+1)
            if line == "7":
               line = "S"
            a.id = a.id[:3]+line
            subwayDictionary[a.id] = a                         # Add station with correct ID
            #print a.id
        #print a.id+" "+subwayDictionary[a.id].name


        b = a
G.remove_node("a")
'''Lines B,D,N,Q,R,W graph'''
for i in ["B","D","N","Q","R","W"]:
    with open('Line'+i+'.csv') as file:
        readCsv = csv.reader(file, delimiter=',')
        temp = readCsv.next()
        c = station(str(temp[0]+i),temp[1],temp[5], row[2], row[3])
        subwayDictionary[str(temp[0]+i)] = c
        for row in readCsv:
                row[0] = row[0]+i

                d = station(str(row[0]),row[1],row[5], row[2], row[3])

                for h in ["1", "2", "3", "4", "5", "6", "S","B","D","N","Q","R","W"]:
                    if (str(str(row[0][:3]) + h) in subwayDictionary) and (str(str(row[0][:3]) + h) != str(row[0])):
                        connect = subwayDictionary[str(str(row[0][:3]) + h)]
                        #print "Connecting: ",d.id," ",connect.id
                        G.add_edge(d.id, connect.id, weight=0)

                subwayDictionary[str(row[0])] = d
                stations.append(a)
                G.add_edge(d.id,c.id, weight =1)
                c=d
'''Connecting Same Station with multiple ids
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
'''
for i in ["1", "2", "3", "4", "5", "6","B","D","N","Q","R","W"]:
    for j in ["1", "2", "3", "4", "5", "6","B","D","N","Q","R","W"]:
        ''' if (str("901"+i) in subwayDictionary) and (str("631"+j) in subwayDictionary):
            G.add_edge(str("901"+i),str("631"+j), weight = 0)
        if (str("127" + i) in subwayDictionary) and (str("902" + j) in subwayDictionary):
            G.add_edge(str("127" + i), str("902" + j), weight=0)
        if (str("R16" + i) in subwayDictionary) and (str("901" + j) in subwayDictionary):
            G.add_edge(str("R16" + i), str("901" + j), weight=0)'''
        if (str("R17" + i) in subwayDictionary) and (str("D17" + j) in subwayDictionary):
            G.add_edge(str("R17" + i), str("D17" + j), weight=0)
        if (str("R20" + i) in subwayDictionary) and (str("635" + j) in subwayDictionary):
            G.add_edge(str("R20" + i), str("635" + j), weight=0)
        if (str("R23" + i) in subwayDictionary) and (str("Q01" + j) in subwayDictionary):
            G.add_edge(str("R23" + i), str("Q01" + j), weight=0)
        if (str("639" + i) in subwayDictionary) and (str("135" + j) in subwayDictionary):
            G.add_edge(str("639" + i), str("135" + j), weight=0)
        if (str("235" + i) in subwayDictionary) and (str("D24" + j) in subwayDictionary):
            G.add_edge(str("235" + i), str("D24" + j), weight=0)
        if (str("R31" + i) in subwayDictionary) and (str("235" + j) in subwayDictionary):
            G.add_edge(str("R31" + i), str("235" + j), weight=0)
        if (str("A24" + i) in subwayDictionary) and (str("125" + j) in subwayDictionary):
            G.add_edge(str("A24" + i), str("125" + j), weight=0)

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
print subwayDictionary["6016"].name
#for i in range(len(D[0])):
#    print subwayDictionary[D[0].nodes()[i]].name
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