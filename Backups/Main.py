import RPi.GPIO as GPIO
from flask import Flask, render_template
import dht11
import time

app = Flask(__name__)
ledPin = 5
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setwarnings(False)


@app.route('/')
def index():
	GPIO.output(ledPin, GPIO.HIGH)
	return render_template('index.html')


@app.route('/on')
def on(): # Blinks LED 5 times
	"""x = 0
	while x<5:"""
	for _ in xrange(5):
		GPIO.output(ledPin, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(ledPin, GPIO.LOW)
		time.sleep(1)
		
        return "All good"
@app.route('/temp')
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


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
