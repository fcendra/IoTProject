from picamera import picamera
import time

camera = PiCamera()

#uncomment the following line to rotate the image if your preview was upside-down!
#camera.rotation = 180

camera.start_preview()
time.sleep(5)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()

