from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()
ball_position = [3, 3]
ball_velocity = [1, 1]
colorList = [(255,0,0),(255,165,0),(255,255,0),(0,255,0),
              (0,0,255),(238,130,238)]
randrange = random.randrange
def ballColor(color):
     sense.set_pixel(ball_position[0], ball_position[1], color)

colorIndex = 0

while True:
    sleep(0.5)
    color = colorList[colorIndex % len(colorList)]
    ball_position[0] = random.randint(ball_position[0] -1,ball_position[0]+1)
    ball_position[1] = random.randint(ball_position[1] -1,ball_position[1]+1)
    sense.clear()
    ballColor(color)
    colorIndex += 1