import RPi.GPIO as GPIO
import time

def main():
    #for _ in xrange(5):
        TRIG = 7
        ECHO = 11

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)
        GPIO.setwarnings(False)

        GPIO.output(TRIG, False)
        time.sleep(2)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO)==0 :
                pulseStart=time.time()
        
        while GPIO.input(ECHO)==1 :
                pulseEnd=time.time()

        pulseDuration = pulseEnd - pulseStart
        distance = pulseDuration * 17150
        distance = round(distance, 2)
       # print """Distance: %d cm""" % (distance)
        GPIO.cleanup()
        return distance

if __name__ == "__main__":
    x = main()
    print( x )
