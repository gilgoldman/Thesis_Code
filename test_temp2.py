#!/usr/bin/python
import sys
import Adafruit_DHT

temp_list = [] # list to hold temperatures
hum_list = []
count = 10 # number of cycles

#while True:
#    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
#    print '''Temp: {0:0.1f} C  Humidity: {1:0.1f} %'''.format(temperature, humidity)

for _ in range(count):
    humidity, temperature = Adafruit_DHT.read_retry(11, 4) # 4 is the BCM number of pin 7
    temp_list.append(temperature)
    print temperature
    hum_list.append(humidity)
    print humidity

temp_avg = (float(sum(temp_list)))/(float(len(temp_list)))
hum_avg = float(sum(hum_list))/float(len(hum_list))

print temp_avg, hum_avg

#print "Average temperature is: ", temp_avg, "C"
#print "Average humidity is : ", hum_avg, "%"
