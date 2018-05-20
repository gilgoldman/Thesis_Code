#!/usr/bin/python
import sys
import Adafruit_DHT

temp_list = [] # list to hold temperatures
hum_list = []
count = 10 # number of cycles

#while True:
#    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
#    print '''Temp: {0:0.1f} C  Humidity: {1:0.1f} %'''.format(temperature, humidity)
def main():
    for _ in range(count):
	humidity, temperature = Adafruit_DHT.read_retry(11, 4) # 4 is the BCM number of pin 7
	temp_list.append(temperature)
	hum_list.append(humidity)

    temp_avg = (float(sum(temp_list)))/(float(len(temp_list)))
    hum_avg = float(sum(hum_list))/float(len(hum_list))

    return temp_avg
#    temp_in_f = 1.8*temp_avg + 32
#    print temp_in_f
#    return temp_in_f
#print "Average temperature is: ", temp_avg, "C"
#print "Average humidity is : ", hum_avg, "%"

if __name__ == "__main__":
    x = main()
    print( x )

