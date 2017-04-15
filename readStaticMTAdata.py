
a={}
with open('stop_times.txt') as trips:
    for row in trips:
        temp = row.split(',')
        stationId =  temp[3]
        arrivalTime = temp[1]
        uniqueTripID = row.split(',')[0][13:]
        print uniqueTripID
        if(uniqueTripID in a):
            a[uniqueTripID][stationId] = arrivalTime
        else:
            a[uniqueTripID] = {}
            a[uniqueTripID][stationId] = arrivalTime

import pickle
newfile = open("stopTimesData.pkl","wb")
pickle.dump(a,newfile)
