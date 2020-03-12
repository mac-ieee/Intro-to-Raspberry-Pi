from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO

camera = PiCamera()

# 3. Displaying the camera preview
# camera.rotation = 0
# camera.start_preview(alpha=200)
# sleep(2)
# 4. Taking still pictures
# a. 
# camera.capture('./test.jpg')
# camera.stop_preview()

# b. 
# camera.start_preview(alpha=200)
# for i in range(5):
	# sleep(2)
	# camera.capture('./image%s.jpg' % i)
	# # the "%s" is used to name each image differently using the "%i"
	# # "%s" is replaced by the loop's index (0-4) in the file name
	# camera.rotation = 90
#camera.stop_preview()

# 6. Mini-project: DIY Camera
#GPIO.setmode(GPIO.BOARD)
#capturePin = 12
#GPIO.setup(capturePin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
#
#while True:
#    if GPIO.input(12) == 0:
#        camera.start_preview(alpha=200)
#        sleep(2)
#        camera.capture('./buttonpic.jpg')
#        camera.stop_preview()

# 7. Recording Video
#camera.start_preview()
#camera.start_recording('./testvideo.h264')
#sleep(9)
#camera.stop_recording()
#camera.stop_preview()


##################################
# 8. Mini-project: DIY Camcorder #
##################################

#GPIO.setmode(GPIO.BOARD)
#capturePin = 12
#capturePin2 = 11
#capturePin3 = 13
#GPIO.setup(capturePin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
#GPIO.setup(capturePin2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
#GPIO.setup(capturePin3,GPIO.IN,pull_up_down=GPIO.PUD_UP)
#
#while True:
#    if GPIO.input(12) == 0:
#        camera.start_preview()
#        camera.start_recording('./buttonvideo.h264')
#        while True:
#            sleep(0.1) #add delay so while loop isn't taking resources
#            if GPIO.input(11) == 0:
#                camera.stop_recording()
#                camera.stop_preview()
#                break
#        break
