from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

LedPin = 4

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOARD)  # numbers GPIO by location
GPIO.setup(LedPin, GPIO.OUT) # Set LedPin mode to output
GPIO.output(LedPin, GPIO.HIGH)
            
@app.route('/')
def index():
#	return "Hello! Welcome to R2Beer2's webpage!"
	return render_template('index.html')


@app.route('/Blinker')
def Blinker():  
    	GPIO.output(LedPin, GPIO.HIGH)
#    	return "Oh Shiiiiiit"

@app.route('/Off')
def Off():  
	GPIO.output(LedPin, GPIO.LOW)
#	return "Aaaaaand it's gone"


if __name__  == '__main__':
	app.run(debug=True, host='0.0.0.0')

