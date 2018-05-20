import RPi.GPIO as GPIO
import time
import numpy
import Temp


def dist():
    result_list = [] # a list to be used in calculation of average
    count = 100  # Number of iterations
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

#	print "Distance:", distance, "cm"
        GPIO.cleanup()

    avg = (float(sum(result_list)))/(float(len(result_list))) # Calculates the measurement average
    avg = round(avg, 4)
    std = numpy.std(result_list, ddof=1)
    std = round(std, 6)
 #   avg_str = "The average distance is: ", avg, 
 #   std_str = "The Standard deviation is: ", std
 #   str_conv1 = str(avg_str)
 #   str_conv2 = str(std_str)
 #   writer.write(str_conv1)
 #   writer.write(str_conv2)
 #   writer.close()
#    print "Average distance: ", avg, "cm"
    print "Standard Deviation: ", std
#    avg = round(avg, 4)
    return avg





def main():
    # Constants:
    cal_temp = 68 # Hydrometer calibration temperature
#    f = 69.8 # fluid temperature constant for testing
#    distance = 9.5 # Distance for tests
    f = Temp.main()
    distance = dist()

    # All the Maths!
    sg = 1.11938 - (0.0125*distance) # SG based on linear scale
    num = 1.00130346 - 1.34722124*(10**(-4))*f + 2.04052596*(10**(-6))*(f**2) - 2.32820948*(10**(-9))*(f**3)
    den = 1.00130346 - 1.34722124*(10**(-4))*cal_temp + 2.04052596*(10**(-6))*(cal_temp**2) - 2.32820948*(10**(-9))*(cal_temp**3)
    C_g = sg*(num/den) # corrected SG
#    C_g = sg * (1 - 0.00025*(f - cal_temp))
    ABW = 517.4*(1-C_g) + 5084*((1-C_g)**2) + 33503*((1-C_g)**3) # Alcohol by weight
    ABV = (ABW*C_g)/0.791 # Alcohol by volume




    print "Temp in c is: ", f
    print "Distance is: ", distance
    print "Specific gravity is: ", sg
    print "Numerator : ", num, " And denominator: ", den
    print "Corrected gravity is: ", C_g
    print "Alcohol by weight: ", ABW
    print "Alcohol by volume: ", ABV

if __name__ == "__main__":
    x = main()
    print( x )
