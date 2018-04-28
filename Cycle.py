import dht11 # This imports dht11 for temperature measurement
import distTest # This imports distest for the distance measurement
from datetime import datetime # For time stamps to the database
import numpy as np # For fancy math
import os
from pathlib import Path
import RPi.GPIO as GPIO # For RasPi Pin control
import sqlite3 # Database
import time # ...guess


# This function checks if the "On" signal is given from the
# web page. If it is, it runs everything
def listener():
    x = False
    while (x == False): # This loop assures the code runs until the signal is given
        text_test = Path("/home/pi/Thesis_Code/Test_Signal.txt")
        if text_test.is_file(): # Test if file exists
	    boop = open("Test_Signal.txt", "r")
	    msg = boop.read()
	    if (msg == "On"): # Checks if the signal was correctly given
		x = True
		Cycle()
	    else:  # If Signal is wrong, delete file
		try:
	            os.remove("Test_Signal.txt")
#		    print "Signal was wrong, file deleted"
	        except OSError:
        	    pass
        else:
	    time.sleep(2)
	    print "Waiting..." # Was here for debugging

# This is where the action happens!
def Cycle():
    print "Success!"

listener()
