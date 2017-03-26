
from google.transit import gtfs_realtime_pb2
import urllib

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
    feed = gtfs_realtime_pb2.FeedMessage()
    response = urllib.urlopen('http://datamine.mta.info/mta_esi.php?key=44fe903c249d311125b5bc56d79ab7ac')
    feed.ParseFromString(response.read())
    ## looping the content downloaded
    tmpSys = datetime.datetime.strftime(datetime.datetime.now() ,'%Y-%m-%d %H:%M:%S')
    i = 1

    for entity in feed.entity:
        if entity.HasField('trip_update'):
            ## trip update: 3 data characterisitcs
            TripIdi = entity.trip_update.trip.trip_id
            Routei = entity.trip_update.trip.route_id
            ## looking to record first 2 predicted arrival time
            ## looking to record first 2 predicted arrival time  ArriveTime=[]
            stop_id=[]

            tripcomplete=[]
            p3trip = min(len(entity.trip_update.stop_time_update),3)
            j=0
            while j < p3trip:
                tripcomplete = []
                # print j
                ArrivalTime = entity.trip_update.stop_time_update[j].arrival.time
                stop_id = entity.trip_update.stop_time_update[j].stop_id
                station_nth = j
                tripcomplete.extend([tmpSys,TripIdi, Routei, station_nth, stop_id, ArrivalTime] )
                #print tmpSys[11:19],"   ",TripIdi,"   ",stop_id,"   ",time.ctime(ArrivalTime)[11:]
                if(time.ctime(ArrivalTime)[20:]!="1969"):
                    tripstr = [TripIdi,stop_id,time.ctime(ArrivalTime)[11:19]]
                    newfile.write(tripstr[0]+" "+tripstr[1]+" "+tripstr[2])
                    newfile.write("\n")
                realtimedata.append([tripstr[0],tripstr[1],tripstr[2]])
                s1 = tmpSys[11:19]
                s2 = time.ctime(ArrivalTime)[11:19]
                #print timediff(s1,s2)


                j+=1



"""while True:
    try:
        loopdwlmta(1)
    except:
        continue
    time.sleep(30)
"""
loopdwlmta(1)
file = open("stopTimesData.pkl","rb")
stopTimesData = pickle.load(file)
for i in realtimedata:
    if(i[0] in stopTimesData):
        s1 = stopTimesData[i[0]][i[1]]
        s2 = i[2]
        delay = float(timediff(s1, s2))

        print "TripId: "+i[0]+" Station ID: "+i[1]+" Original Time: "+stopTimesData[i[0]][i[1]]+" Current Arrival Time: "+i[2]+" Delay: ",delay






