
from google.transit import gtfs_realtime_pb2
import urllib
import datetime
import time

def savefile(listitems):
    with open('mta.txt' ,'a') as f:
        f.write(listitems + '\n')

def timediff(s1,s2):
    from datetime import datetime
    FMT = '%H:%M:%S'
    tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
    return tdelta

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
                print tmpSys[11:19],"   ",TripIdi,"   ",stop_id,"   ",time.ctime(ArrivalTime)[11:]
                s1 = tmpSys[11:19]
                s2 = time.ctime(ArrivalTime)[11:19]
                print timediff(s1,s2)
                #print tripcomplete
                #print tripcomplete
                tripcomplstr = ','.join([str(i) for i in tripcomplete])

                savefile(tripcomplstr)
                j+=1




while True:
    try:
        loopdwlmta(1)
    except:
        continue
    time.sleep(30)







