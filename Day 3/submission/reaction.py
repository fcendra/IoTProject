import RPi.GPIO as GPIO
import time
import random
player_1 = input("Please enter the left player's name: ")
player_2 = input("Please enter the right player's name: ")
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
led = 4
GPIO.setup(led,GPIO.OUT)
GPIO.output(led,0)
time.sleep(random.uniform(1,5))
GPIO.output(led,1)
left_button = 14
right_button = 15
GPIO.setup(left_button,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(right_button,GPIO.IN,GPIO.PUD_UP)
try:
    while True:
        if(GPIO.input(14)) == False:
            print(player_1,'wins!')
            break
        if(GPIO.input(15)) == False:
            print(player_2,'wins!')
            break
except KeyboardInterrupt:
    print("CTRL-C: Terminating program.")
finally:
    print("Cleaning up GPIO...")
    GPIO.cleanup()
