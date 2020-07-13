from sense_hat import SenseHat
from time import sleep
import random
sense = SenseHat()

ball_position = [3, 3] # coordinates of the starting position
white = (255, 255, 255)
sense.set_pixel(ball_position[0], ball_position[1], white)

while True:
  sleep(1)	# sleep for 1 second
  ball_position[0] = random.randint(0, 7) # generate a new x-position
  ball_position[1] = random.randint(0, 7) # generate a new y-position
  sense.clear()
  sense.set_pixel(ball_position[0], ball_position[1], white)
