#!/usr/bin/python
#import dht11 # This imports dht11 for temperature measurement
import distTest # This imports distest for the distance measurement
import ABV_test # the SG
from datetime import datetime # For time stamps to the database
import argparse
from influxdb import InfluxDBClient
import json
import math
import requests
import sys
from time import sleep
import RPi.GPIO as GPIO

#GPIO.setmode (GPIO.BOARD)
#GPIO.setup(18,GPIO.IN)
GPIO.setwarnings(False)

# First Database, will hold Distance ("Alcohol By Volume")
IP = "192.168.0.91" # The IP of the machine hosting your influxdb instance
#IP = "169.254.121.197"
DB = "Test" # The database to write to, has to exist
USER = "logs_user" # The influxdb user to authenticate with
PASSWORD = "1234" # The password of that user 
TIME = 5 # Delay in seconds between two consecutive updates 

# Second Database, Will hold SG
#IP = "192.168.0.91" # The IP of the machine hosting your influxdb instance
DB2 = "logs" # The database to write to, has to exist
#USER = "logs_user" # The influxdb user to authenticate with
#PASSWORD = "1234" # The password of that user 
#TIME = 5 # Delay in seconds between two consecutive updates 


#while True: 
#    v = 'Button value=%s' % GPIO.input(18) 
#    r =  requests.post("http://%s:8086/write?db=%s" %(IP, DB), auth=(USER, PASSWORD), data=v) 
#        if r.status_code != 204: 
#        print ('Failed to add point to influxdb (%d) - aborting.' %r.status_code) 
#        sys.exit(1) 
#    sleep(TIME)

while True:
    ABV_value = "ABV value=%s" % distTest.main()
#    ABV_value = "ABV value=%s" % ABV_test.dist()
    SG = "Corrected_Gravity value=%s" % ABV_test.main()
    print ABV_value
    print SG

    r_a = requests.post("http://%s:8086/write?db=%s" %(IP, DB), auth=(USER, PASSWORD), data=ABV_value)
    if r_a.status_code != 204:
	print r_a.text
        print ('Failed to add point to influxdb (%d) - aborting.' %r_a.status_code)
        sys.exit(1)
    sleep(TIME)

    r_b = requests.post("http://%s:8086/write?db=%s" %(IP, DB2), auth=(USER, PASSWORD), data=SG)
    if r_b.status_code != 204:
	print r_b.read
        print ('Failed to add point to influxdb (%d) - aborting.' %r_b.status_code)
	sys.exit(1)
    sleep(TIME)
