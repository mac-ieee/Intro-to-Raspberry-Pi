######################################
# 4.b Taking multiple pictures in a row
######################################

from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO

camera = PiCamera()

camera.start_preview()
for i in range(5):
       sleep(2)
       camera.capture('./image%s.jpg' % i)
       # the "%s" is used to name each image differently using the "%i"
       # "%s" is replaced by the loop's index (0-4) in the file name
camera.stop_preview()
