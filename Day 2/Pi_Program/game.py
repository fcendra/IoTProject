from time import sleep
from sense_hat import SenseHat

sense = SenseHat()

ball_position = [3, 3]
ball_velocity = [1, 1]
bat_pos = 4

def draw_bat(color):
  r = color[0
  g = color[1]
  b = color[2]]
  sense.set_pixel(0, bat_pos, r,g,b)
  sense.set_pixel(0, bat_pos+1, r,g,b)
  sense.set_pixel(0, bat_pos-1,r,g,b)
  
def move_up(event):
  global bat_pos
  if bat_pos > 1 and event.action=='pressed':
    bat_pos -= 1
    
def move_down(event):
  global bat_pos
  if bat_pos < 6 and event.action=='pressed':
    bat_pos += 1
    
def draw_ball(count):
  global counter
  counter = 0
  # Draws the ball pixel
  sense.set_pixel(ball_position[0], ball_position[1], 255, 255, 255)
  # Moves the ball to the next position
  ball_position[0] += ball_velocity[0]
  ball_position[1] += ball_velocity[1]
    
  if ball_position[1] == 0 or ball_position[1] == 7: 
    ball_velocity[1] = -ball_velocity[1]
  if ball_position[0] == 0 or ball_position[0] == 7:
    ball_velocity[0] = -ball_velocity[0]
  if ball_position[0] == 1 and bat_pos - 1 <= ball_position[1] <= bat_pos + 1:
    ball_velocity[0] = -ball_velocity[0]
    counter += 1
    return counter
        
sense.stick.direction_up = move_up
sense.stick.direction_down = move_down
colorLevel = [(255,0,0),(255,165,0),(255,255,0),(0,255,0),
              (0,0,255),(238,130,238)] #from red to violet (low level to high level)
countIndex = 0
speedIndex = 0.5
count = 0 #to state how many succesful draw between the bat and the ball
while True:
  sense.clear(0, 0, 0)
  color = colorList[colorIndex % len(colorList)]
  draw_bat(color)
  draw_ball(count)
  sleep(speedIndex)
  if counter == 1:
    count += 1
  if count == 7 and colorIndex < len(colorList) - 1:
    colorIndex += 1
    speedIndex -= 0.075
    count = 0
  if ball_position[0] == 0:
    sense.show_message("You lose", text_colour = (255,0,0))
    count = 0
    ball_position = [3, 3]
    colorIndex = 0
    speedIndex = 0.5
    
  print(count)
