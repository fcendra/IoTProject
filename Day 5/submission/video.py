from picamera import picamera
import time
camera = PiCamera()

#uncomment the following line if the preview was upside-down
#camera.rotation = 180

camera.start_preview()
camera.start_recording('/home/pi/video/h264')
time.sleep(10)
camera.stop_recording()
camera.stop_preview()

