import speedtest
import csv 
import datetime

with open('speedtest.csv', 'w') as f:
    #create heading for csv
    f.write('time,download,upload\n')    
    
with open('speedtest.csv', 'a') as f:
    while True:
        st = speedtest.Speedtest() 
        print(st.download())
        print(st.upload())

        writer = csv.writer(f)
        current_time = datetime.datetime.now()
        writer.writerow([current_time, st.download(), st.upload()])    