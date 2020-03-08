
#This imports the necessary libraries to access the pins on the Pi
import RPi.GPIO as GPIO 

#This tells Python and the Pi that we're using the physical pin numbering scheme
GPIO.setmode(GPIO.BOARD)

#Alternatively, you can use the GPIO numbering scheme by using the line below
# GPIO.setmode(GPIO.BCM)
 
led =11 
#According to the physical pin numbering scheme, we want pin 11 to be the output. If using the GPIO
#numbering scheme, you would use “17” to reference the same pin

#configure pin 11 as an output
GPIO.setup(led,GPIO.OUT)

#This sends a high output to pin 11 and turns the LED on
GPIO.output(led,True)