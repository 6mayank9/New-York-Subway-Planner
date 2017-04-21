import csv
import networkx as nx


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
for i in ["1", "2", "3", "4", "5", "6"]:
    for j in ["1", "2", "3", "4", "5", "6"]:
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
newfile = open("allDelaydumps.pkl","wb")           # Dumps the graph and dictionary to a file
pickle.dump([subwayDictionary,G],newfile)

print subwayDictionary["6016"].name

