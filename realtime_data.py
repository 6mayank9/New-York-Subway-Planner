
from google.transit import gtfs_realtime_pb2
import urllib
import time
import datetime

def savefile(listitems):
    with open('mta.txt' ,'a') as f:
        f.write(listitems + '\n')

def loopdwlmta(x):	## send request to api mta.info using my own key
    feed = gtfs_realtime_pb2.FeedMessage()
    response = urllib.urlopen('http://datamine.mta.info/mta_esi.php?key=5a8f6f4375e9f4bdea9b0c86afeaf911')
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
                # print tripcomplete
                print tripcomplete, type(tripcomplete)
                tripcomplstr = ','.join([str(i) for i in tripcomplete])
                savefile(tripcomplstr)
                j+=1

import time


while True:
    try:
        loopdwlmta(1)
    except:
        continue
    time.sleep(300)







