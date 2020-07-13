import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#GPIO ports
red_led = 13
green_led = 26
red_signal_led = 20
push_button = 19
#GPIO setup
GPIO.setup(red_led,GPIO.OUT)
GPIO.setup(green_led,GPIO.OUT)
GPIO.setup(red_signal_led,GPIO.OUT)
GPIO.setup(push_button,GPIO.IN,GPIO.PUD_UP)
def time_press(push_button):
    while True:
        if GPIO.input(push_button)==False:
            start_time = time.time()
            while (GPIO.input(push_button))==False:
                pass
            end_time = time.time()
            interval = end_time - start_time
            return interval
def activation(interval):
    if float(interval)>=0.5:
        return True
def green_on(green_led,count):
    GPIO.output(green_led,1)
    time.sleep(5)
    for i in range (1,12):
        if i % 2 == 0:
            GPIO.output(green_led,1)
            time.sleep(0.25)
        else:
            GPIO.output(green_led,0)
            time.sleep(0.25)
def red_on(red_led,red_signal_led,count):
    GPIO.output(red_led,1)
    start_time = time.time()
    interval = time_press(push_button)
    buttonPressed = False
    while buttonPressed == False:
        buttonPressed = activation(interval)
    end_time = time.time()
    difference = end_time - start_time
    if difference < 5:
        GPIO.output(red_signal_led,1)
        time.sleep((5-difference)+3)
    else:
    #elif difference >= 5:
        GPIO.output(red_signal_led,1)
        time.sleep(3)
count = 0
try:
    while True:
        if count % 2 == 0:
            GPIO.output(red_led,0)
            GPIO.output(red_signal_led,0)
            green_on(green_led,count)
        else:
            GPIO.output(green_led,0)
            red_on(red_led,red_signal_led,count)
        count += 1
except KeyboardInterrupt:
    print("CTRL-C: Terminating program.")
finally:
    print("Cleaning up GPIO...")
    GPIO.cleanup()



