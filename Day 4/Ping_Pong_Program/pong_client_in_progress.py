# Pong Client

import socket
from time import sleep
from sense_hat import SenseHat

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('192.168.1.1', 3542)
sock.connect(server_address)

sense = SenseHat()

y = 4 #bat position
opponent = 4 #position of oppenent's bat
ball_position = [3, 3]
ball_velocity = [1, 1]

def draw_bat():
    sense.set_pixel(7, y, 0, 255, 0)
    sense.set_pixel(7, y + 1, 0, 255, 0)
    sense.set_pixel(7, y - 1, 0, 255, 0)
    sense.set_pixel(0, opponent, 0, 0, 255)
    sense.set_pixel(0, opponent + 1, 0, 0, 255)
    sense.set_pixel(0, opponent - 1, 0, 0, 255)

def move_up(event):
    global y
    if y > 1 and event.action=='pressed':
        y -= 1

def move_down(event):
    global y
    if y < 6 and event.action=='pressed':
        y += 1

def draw_ball():
#def draw_ball(current_color, counter_success_phase2): #in progress, with change color function
    global ball_position
    #global ball_position, opponent, counter_success_phase1 #in progress, change the upper code when its done
    # Draws the ball pixel
    #counter_success_phase1 = 0 #in progress 
    #r = color[0] #in progress
    #g = color[1] #in progress
    #b = color[2] #in progress
    sense.set_pixel(ball_position[0], ball_position[1], 255, 255, 255)
     #sense.set_pixel(ball_position[0], ball_position[1],r,g,b) #in progress to change color of the ball
    # # Moves the ball to the next position
    # ball_position[0] += ball_velocity[0]
    # ball_position[1] += ball_velocity[1]
    # # Ball hits player's bat
    # if ball_position[0] == 1 and y - 1 <= ball_position[1] <= y + 1:
    #     ball_velocity[0] = -ball_velocity[0]
    # # Ball hits opponent's bat
    # if ball_position[0] == 6 and opponent - 1 <= ball_position[1] <= opponent + 1:
    #     ball_velocity[0] = -ball_velocity[0]
    # # Ball hits side walls
    # if ball_position[1] == 0 or ball_position[1] == 7:
    #     ball_velocity[1] = -ball_velocity[1]
    # # Ball is not rebounced by either bat
    # if ball_position[0] == 0 or ball_position[0] == 7:
    #     ball_velocity[0] = -ball_velocity[0]
        #counter_success_phase1 += 1 #in progress to indicate succesfull attempt phase 1
        #return counter_success_phase1 #in progress always reset to 0

sense.stick.direction_up = move_up
sense.stick.direction_down = move_down
#colorList = [(255,0,0),(255,165,0),(255,255,0),(0,255,0),(0,0,255),(238,130,238)] #in progress Color_list
#counter_success_phase2 = 0 #in progress to indicate successfull attemp phase 2
#speed_index = 0.5 #in progress speed initiation
#colorIndex = 0 #in progress, color index
counter = 0

while True:
    sock.send(str(y).encode("utf-8"))
    incoming_y = sock.recv(1024)
    #current_color = colorList[colorIndex % len(colorList)] #in progress, to state current color for ball color
    #draw_ball(current_color, counter_success_phase2) #in progress
    if incoming_y:
        data = incoming_y.decode("utf-8")
        array = data.split(',')
        if len(array) == 3:
            opponent = int(array[0])
            ball_position[0] = int(array[1])
            ball_position[1] = int(array[2])
    #if counter_success_phase1 == 1:
        #counter_success_phase2 += 1 #in progress count until 5 then ball color changenand speed change
    #if counter_success_phase2 == 5 and color_index <len(colorList) - 1:
        #colorIndex += 1 #in progress, when counter phase 2 = 5, change color
        #speed_index -= 0.075 #in progress, change speed
        #counter_success_phase2 = 0 #in progress, reset counter
    if counter >= 5:
        sense.clear(0, 0, 0)
        draw_bat()
        draw_ball()
        counter = 0
    else:
        counter += 1
    #if ball_position[0] == 0:
        #counter_success_phase2 = 0 #in progress, reset counter
        #ball_position = [3,3] #in progress,reset ball intialize position
        #colorIndex = 0 #in progress, color index reset
        #speed_index = 0.5 #n progress, speed reset
        #sense.show_message ("you lose!", text_colour = (255,0,0)) #in progress for indication lose
        #return False #in progress to indicate opponent to print "Won!"
    #if ball_position_opponent[0] == 0:
        #counter_success_phase2 = 0 #in progress, reset counter
        #ball_position = [3,3] #in progress, when opponent lose, reset ball position
        #colorIndex = 0 #in progress, color index reset
        #speed_index = 0.5 #n progress, speed reset
        #sense.show_message ("you Won!", text_colour = (255,0,0)) #in progress for indication Won
    
    sleep(0.05)
    #sleep(speed_index) #in progress, change the upper code to this one
