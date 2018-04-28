import distTest # This imports distest for the distance measurement
import dht11
from datetime import datetime
from flask import Flask, render_template # Web Framework
import numpy as np # For fancy math
import RPi.GPIO as GPIO # For RasPi Pin control
import sqlite3 # Database
import time # guess

app = Flask(__name__)

# Pin assignments:
# General pin assignments
ERRORLED = 5

# For HC-sr04:
TRIG = 7
ECHO = 11

# Function definitions and calls:

# Retrieves Temperature and humidity from DHT11:
def temp():
    instance = dht11.DHT11(pin=7)
    result = instance.read()
    if result.is_valid():
        #A = "Temperature: %d C" % result.temperature # Is this line really relevant?
        #B = "Humidity: %d %%" % result.humidity # Is this line really relevant?
        # return ("Temperature: %d C" % result.temperature + "Humidity: %d %%" % result.humidity)
        # print """ Temperature: %d C Humidity: %d""" % (result.temperature, result.humidity)
        #return """Temperature: %d C <br/>Humidity: %d""" % (result.temperature, result.humidity)
        return (result.temperature, result.humidity)

# Retrieves distance from HC-sr04
def distance_read():
    x = distTest.main()
    # This will need to be determined experimentally
    # Only way to do this right would be to measure steps
    # such as 0%, 5%, etc and derive from that some relation
    # To be continued!
    return (distTest.main())

# Store data in database
def data_into_database():
    ts = time.time()
    dist_now = distTest.main()
    time_now = datetime.now()
    

# Prepare board
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Pin Setup
GPIO.setup(ERRORLED, GPIO.OUT) # Assigns an output pin For LED
GPIO.setup(TRIG, GPIO.OUT) # Sets the trig signal for hc-sr04 as output
GPIO.setup(ECHO, GPIO.IN) # Sets a pin for input for echo

# Set up the database
conn = sqlite3.connect('sensor_database.db') # Connects to the DB
# Creates the relevant tables. Created by default, uncomment if creating a fresh install
#conn.execute('''CREATE TABLE sensors
#    (timestamp DATETIME, 
#    distance INT, 
#    temperature INT,
#    humidity INT);''')
# 
#conn.commmit() # Commits changes. Just here to remember
conn.close() # Close database connection to save RAM




# This is the main page - there's a button here which will start the process
@app.route('/')
def index():
    
    return render_template('index.html')

# This is just a test for the HC-sr04 functionality
@app.route('/distance_test')
def distance_test():
    x = distance_read()
    return """ Distance: %d cm """ % (x)

# This is where the magic will happen!
# Or... where the graphs will apear and measurements taken
@app.route('/on')
def led_on():
#    GPIO.output(ERRORLED, GPIO.HIGH)
    return "Are you feeling it now Mr. Krabs?"


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
