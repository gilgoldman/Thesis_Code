import RPi.GPIO as GPIO
import time
import numpy

def main():
    result_list = [] # a list to be used in calculation of average
    count = 10  # Number of iterations
#    writer = open("Measurement_14_mm.txt", "w") # opens a text file
    for _ in range(count):
	TRIG = 23 # BCM value of pin 16
	ECHO = 24 # BCM value of pin 18
		  # Remember that ECHO needs a voltage divider

	GPIO.setmode(GPIO.BCM)
        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)
        GPIO.setwarnings(False)

        GPIO.output(TRIG, False)
        time.sleep(2)
#	time.sleep(1) # Still works with 1 second delay - why use 2?
		      # Cause not so accurate. noise in measurement noticeable?
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO)==0 :
                pulseStart=time.time()

        while GPIO.input(ECHO)==1 :
                pulseEnd=time.time()

        pulseDuration = pulseEnd - pulseStart
        distance = pulseDuration * 17150
        distance = round(distance, 3)

	result_list.append(distance) # Appends results to the list

#	diststr = str(distance) # convert distance to string
#	writer.write(diststr) # write distance string to the open text file
#	writer.write("\n") # write a new line 

	print "Distance:", distance, "cm"
        GPIO.cleanup()

    avg = (float(sum(result_list)))/(float(len(result_list))) # Calculates the measurement average
#    avg = avg/3 # A shortened avg to simulate alcohol percentage
    avg = round(avg, 2)
    std = numpy.std(result_list, ddof=1)
    std = round(std, 6)
 #   avg_str = "The average distance is: ", avg, 
 #   std_str = "The Standard deviation is: ", std
 #   str_conv1 = str(avg_str)
 #   str_conv2 = str(std_str)
 #   writer.write(str_conv1)
 #   writer.write(str_conv2)
 #   writer.close()
    print "Average distance: ", avg, "cm"
    print "Standard Deviation: ", std

    print "Beep"
#    return avg

if __name__ == "__main__":
    x = main()
    print( x )
