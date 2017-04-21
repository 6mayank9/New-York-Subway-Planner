import csv
import networkx as nx
class station:                                # station class to store attributes of each subway station
    def __init__(self, stop_id, stop_name, trains, latitude, longitude):
        self.id = stop_id                     # Unique Station ID
        self.name = stop_name                 # Station name
        self.trains = trains                  # List of trains at this staion
        self.longitude = longitude
        self.latitude = latitude


# change input for the stations that you want to count crowdedness
a={}
with open('turnstile_170408.txt') as turnstile:
    for row in turnstile:

        temp = row.split(',')
        turnstileid = temp[1]
        time = temp[6] + temp[7]
        entries = int(temp[9])
        exits = int(temp[10])
        if turnstileid not in a:
            a[turnstileid] = {}
        if time not in a[turnstileid]:
            a[turnstileid][time] = 0
        a[turnstileid][time] += abs((entries + exits))

def wieght_for_cowededness(input):
    def crowdedness(x):

        def searchTime(currTime,date):
            currTime = currTime.replace(":","")
            prev = -1
            prevRet = ""
            nextRet = ""
            next = 24
            for key in a[x]:
                if key[:10] == date:
                    #print key[10:].replace(":",""), currTime, prev
                    if (int(key[10:].replace(":","")) <= int(currTime)) and (prev < int(key[10:12].replace(":",""))):
                        prev = int(key[10:12])
                        #print prev
                        prevRet = key
                    if int(key[10:].replace(":","")) > int(currTime) and next > int(key[10:12].replace(":","")):
                        next = int(key[10:12])
                        nextRet = key
                    #print key[10:12]
            if nextRet == "":
                nextRet = prevRet
                list1 = list(nextRet)
                list1[10] = "0"
                if nextRet[3] != "0":
                    list1[3:5] = str(int(nextRet[3:5])+1)
                elif nextRet[3] == "0" and nextRet[4] == "9":
                    list1[3:5] = str(10)
                else:
                    list1[4] = str(int(nextRet[3:5]) + 1)

                nextRet = "".join(list1)
            return prevRet,nextRet


        if x not in a:
            return 0
        prev,next = searchTime("20:22:40","04/06/2017")
        #print "prev: ",prev," next:",next
        '''if '04/06/201720:00:00' in a[x]:
            crowdedness = int(a[x]['04/06/201720:00:00'] - a[x]['04/06/201716:00:00'])
        elif '04/06/201721:00:00' in a[x]:
            crowdedness = int(a[x]['04/06/201721:00:00'] - a[x]['04/06/201717:00:00'])
        elif '04/06/201722:00:00' in a[x]:
            crowdedness = int(a[x]['04/06/201722:00:00'] - a[x]['04/06/201718:00:00'])
        elif '04/06/201723:00:00' in a[x]:
            crowdedness = int(a[x]['04/06/201723:00:00'] - a[x]['04/06/201719:00:00'])'''
        #print "prev: ", a[x][prev], " next: ", a[x][next]
        crowd = abs(int(a[x][next] - a[x][prev]))
        return crowd

    weight = 0
    #print "abc"
    with open('TurnstileIDtoStationID.csv') as Turnstile:
        reader = csv.DictReader(Turnstile)
        for row in reader:
            if row['stop_id'] == input:
                #print row['Remote']
                weight += crowdedness(row['Remote'])
    return weight

import pickle
filehandler = open("alldumps.pkl","rb")
subwayDictionary,G = pickle.load(filehandler)

for stopid in subwayDictionary.items():
    #print str(stopid[0][:3])
    crowd = str(wieght_for_cowededness(stopid[0][:3]))
    #print " Weight: "+ crowd
    k = G.neighbors(str(stopid[0]))
    for i in range(len(k)):
        if (G[str(stopid[0])][k[i]]['weight'] != 0):
            G[str(stopid[0])][k[i]]['weight'] += int(crowd)

'''print "Weights Updated"
print "Calculating Route...."
route = nx.dijkstra_path(G, "1201", "1202", 'weight')
for s in route:
    print subwayDictionary[s].name
print nx.dijkstra_path_length(G, "1201", "1202", 'weight')'''
def getPath(source,destination):
    route = nx.dijkstra_path(G, source, destination, 'weight')
    length = nx.dijkstra_path_length(G, source, destination, 'weight')
    return route, length

#print wieght_for_cowededness("B22")




