#!/usr/bin/python
import dht11 # This imports dht11 for temperature measurement
import distTest # This imports distest for the distance measurement
from datetime import datetime # For time stamps to the database
import argparse
from influxdb import InfluxDBClient
import json
import math
import requests
import sys
from time import sleep
import RPi.GPIO as GPIO

# Here you should update you own GPIO code
GPIO.setmode (GPIO.BOARD)
GPIO.setup(18,GPIO.IN)
GPIO.setwarnings(False)



IP = "192.168.0.91" # The IP of the machine hosting your influxdb instance
DB = "sensor_logs" # The database to write to, has to exist
USER = "logs_user" # The influxdb user to authenticate with
PASSWORD = "1234" # The password of that user 
TIME = 5 # Delay in seconds between two consecutive updates 
#while True: 
#    v = 'Button value=%s' % GPIO.input(18) 
#    r = requests.post("http://%s:8086/write?db=%s" %(IP, DB), auth=(USER, PASSWORD), data=v) 
#        if r.status_code != 204: 
#        print ('Failed to add point to influxdb (%d) - aborting.' %r.status_code) 
#        sys.exit(1) 
#    sleep(TIME)

