
from google.transit import gtfs_realtime_pb2
import urllib
import networkx as nx
import datetime
import time
import pickle
class station:                                # station class to store attributes of each subway station
    def __init__(self, stop_id, stop_name, trains):
        self.id = stop_id                     # Unique Station ID
        self.name = stop_name                 # Station name
        self.trains = trains                  # List of trains at this staion
filehandler = open("alldumps.pkl","rb")
subwayDictionary,G = pickle.load(filehandler)
newfile = open('realtimedata.txt' ,'w')

def timediff(s1,s2):
    from datetime import datetime
    FMT = '%H:%M:%S'
    tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)

    return tdelta.total_seconds()
realtimedata = []
def loopdwlmta(x):	## send request to api mta.info using my own key
    '''All Lines'''
    feed = gtfs_realtime_pb2.FeedMessage()
    response = [urllib.urlopen('http://datamine.mta.info/mta_esi.php?key=44fe903c249d311125b5bc56d79ab7ac&feed_id=1'),
                urllib.urlopen('http://datamine.mta.info/mta_esi.php?key=44fe903c249d311125b5bc56d79ab7ac&feed_id=16'),
                urllib.urlopen('http://datamine.mta.info/mta_esi.php?key=44fe903c249d311125b5bc56d79ab7ac&feed_id=21')]
    for t in range(len(response)):

        feed.ParseFromString(response[t].read())
        ## looping the content downloaded
        tmpSys = datetime.datetime.strftime(datetime.datetime.now() ,'%Y-%m-%d %H:%M:%S')


        for entity in feed.entity:
            if entity.HasField('trip_update'):
                TripIdi = entity.trip_update.trip.trip_id
                Routei = entity.trip_update.trip.route_id
                p3trip = min(len(entity.trip_update.stop_time_update),3)

                j=0
                while j < p3trip:
                    tripComplete = []
                    ArrivalTime = entity.trip_update.stop_time_update[j].arrival.time
                    stop_id = entity.trip_update.stop_time_update[j].stop_id
                    station_nth = j
                    tripComplete.extend([tmpSys,TripIdi, Routei, station_nth, stop_id, ArrivalTime] )
                    if time.ctime(ArrivalTime)[20:]!="1969":
                        tripstr = [TripIdi,stop_id,time.ctime(ArrivalTime)[11:19]]
                        newfile.write(tripstr[0]+" "+tripstr[1]+" "+tripstr[2])
                        newfile.write("\n")
                    realtimedata.append([tripstr[0],tripstr[1],tripstr[2]])

                    j += 1

"""while True:
    try:
        loopdwlmta(1)
    except:
        continue
    time.sleep(30)
"""
loopdwlmta(1)
staticDatafile = open("stopTimesData.pkl","rb")
stopTimesData = pickle.load(staticDatafile)
for i in realtimedata:
    if i[0] in stopTimesData:
        s1 = stopTimesData[i[0]][i[1]]
        s2 = i[2]
        delay = float(timediff(s1, s2))
        print "TripId: "+i[0]+" Station ID: "+i[1]+" Original Time: "+stopTimesData[i[0]][i[1]]+" Current Arrival Time: "+i[2]+" Delay: ", delay
        if delay > 0 :
            if i[0][7] == "G":
                i[0][7]="S"
            print str(str(i[1][0:3])+i[0][7])
            if(str(str(i[1][0:3])+i[0][7]) in subwayDictionary):
                print "found"
                k = G.neighbors(str(i[1][0:3])+i[0][7])
                for j in range(len(k)):
                    if(G[str(i[1][0:3])+i[0][7]][k[j]]['weight'] != 0):
                        G[str(i[1][0:3])+i[0][7]][k[j]]['weight'] += delay


print "Weights Updated"
print "Calculating Route...."
route =  nx.dijkstra_path(G,"1201","1202",'weight')
for s in route:
    print subwayDictionary[s].name
print nx.dijkstra_path_length(G,"1201","1202",'weight')




