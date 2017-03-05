import csv
import networkx as nx
import matplotlib.pyplot as plt
class station:                                # station class to store attributes of each subway station

    def __init__(self, stop_id, stop_name, trains):
        self.id = stop_id
        self.name = stop_name
        self.trains = trains

G = nx.Graph()
stations = []
b = station("a", "a", "a")
with open('SubwayStops.csv') as csvfile:
    readCsv = csv.reader(csvfile, delimiter=',')
    readCsv.next()
    for row in readCsv:
        a = station(row[0],row[1],row[5])
        if(a.id[0]==b.id[0]):
            G.add_edge(a, b)
        stations.append(a)
        b = a
nx.write_gpickle(G,"subwaygraph.gpickle")
print nx.info(G)
nx.draw(G)
plt.show()