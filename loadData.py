'''Example of how to load the graph and dictionary
'''
import pickle
import realtime_data as rd
import time
rd.loopdwlmta(1)
class station:                                # station class to store attributes of each subway station
    def __init__(self, stop_id, stop_name, trains):
        self.id = stop_id                     # Unique Station ID
        self.name = stop_name                 # Station name
        self.trains = trains                  # List of trains at this staion
filehandler = open("alldumps.pkl","rb")
subwayDictionary,G = pickle.load(filehandler)
k = G.neighbors(subwayDictionary["104"])
#print subwayDictionary["104"].name+" number of neighbors are ",len(k)
#for i in range(len(k)):
#    print k[i].name

#time.sleep(5)
with open("realtimedata.txt",mode='r') as file:
    for line in file:
        content = line.split(" ")
        print line


