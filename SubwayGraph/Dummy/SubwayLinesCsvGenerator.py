import csv


list = ["A","B","C","D","E","F"]
with open('SubwayStops.csv') as csvfile:
    readCsv = csv.reader(csvfile, delimiter=',')
    for row in readCsv:
        for k in list:
            if( str(k) in row[5].split(" ")):
                with open('LineA-F.csv','a') as writefile:
                    for l in row:
                        writefile.write(l+",")
                    writefile.write("\n")
