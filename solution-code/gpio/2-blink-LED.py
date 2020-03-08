
import RPi.GPIO as GPIO
import time #this allows us to introduce delays in our code


GPIO.setmode(GPIO.BOARD) #physical numbering scheme

led = 11 #connect LED to pin 11
GPIO.setup(led,GPIO.OUT) #set pin 11 as output

#get user input and store it as an integer in a variable
blinkNum =int(input(‘How many times do you want to blink?’))

for i in range(blinkNum):
    GPIO.output(led,True) #can also use 1 instead of TRUE to turn on
    time.sleep(1)#delay 1 second
    GPIO.output(led,False)#can also use 0 instead of FALSE to turn off
    time.sleep(1)#delay 1 second
    
GPIO.cleanup()