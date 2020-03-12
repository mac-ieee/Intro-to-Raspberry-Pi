#################################
# 8. Mini-project: DIY Camcorder 
#################################

from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO

camera = PiCamera()

GPIO.setmode(GPIO.BOARD)
capturePin = 12
capturePin2 = 11
capturePin3 = 13
GPIO.setup(capturePin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(capturePin2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(capturePin3,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(12) == 0:
        camera.start_preview()
        camera.start_recording('./diycamcorder.h264')
        while True:
            sleep(0.1) #add delay so while loop isn't taking resources
            if GPIO.input(11) == 0:
                camera.stop_recording()
                camera.stop_preview()
                break
        break
