import RPi.GPIO as GPIO
from flask import Flask, render_template
import dht11
import distTest
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


app = Flask(__name__)

# Variable assignments
ledPin = 5
TRIG = 7
ECHO = 11

# Prepare Board 
#GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

# Pin Assignments
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setwarnings(False)



@app.route('/')
def index():
        GPIO.output(ledPin, GPIO.HIGH)
        return render_template('index.html')


@app.route('/on')
def on(): # Blinks LED 5 times
        for _ in xrange(5):
                GPIO.output(ledPin, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(ledPin, GPIO.LOW)
		time.sleep(1)
        return "All good"

@app.route('/temp')
# Use DHT11 to measure Humidty and Temperature
# Show data on Webpage
# Test, prep for pt100 sensor
def temp():
        instance = dht11.DHT11(pin = 7)
        result = instance.read()
        if result.is_valid():
            A = "Temperature: %d C" % result.temperature
            B = "Humidity: %d %%" % result.humidity
            #return ("Temperature: %d C" % result.temperature + "Humidity: %d %%" % result.humidity)
            #print """ Temperature: %d C
            #Humidity: %d""" % (result.temperature, result.humidity)
            return """Temperature: %d C <br/>Humidity: %d""" % (result.temperature, result.humidity)

@app.route('/dist')
# Use HC-SR04 to measure distance
# Show data on Webpage
# Test for Suagr meter
def dist():
# function to give HC-SR04 sensor a calibrating pulse
	#GPIO.output(TRIG, False)
	#time.sleep(2)
	#GPIO.output(TRIG, True)
	#time.sleep(0.00001)
	#GPIO.output(TRIG, False)
	
	#while GPIO.input(ECHO)==0 :
	#	pulseStart=time.time()
        #while GPIO.input(ECHO)==1 :
        #        pulseEnd=time.time()
        
        #pulseDuration = pulseEnd - pulseStart
        #distance = pulseDuration * 17150
        #distance = round(distance, 2)
        #GPIO.cleanup()
        #return """Distance: %d cm""" % (distance)

        return """Distance: %d cm""" % (distTest.main())
        
                
                

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
