#############################
#   Dim an LED using
#   PWM.
############################


import RPi.GPIO as GPIO 

GPIO.setmode(GPIO.BOARD)

GPIO.setup(led_R, GPIO.OUT) #initialize pin as output 

pwm_R = GPIO.PWM(led_R, 5000) #initialize PWM pin, frequency = 5kHz
pwm_R.start(0) #start pin at 0% duty cycle 

duty = 0 #modify this statement and look at LED

pwm_R.ChangeDutyCycle(duty) 
