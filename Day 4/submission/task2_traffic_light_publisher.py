import paho.mqtt.publish as publish

hostname = "test.mosquitto.org"
port = 1883

topic_state = "PC000/traffic_light/state"

#publish.single(topic_state,payload=1,qos = 0,hostname=hostname,port=port)

###########################################################################################
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#GPIO port
red_led = 13 
green_led = 26
red_signal_led = 20 
push_button = 19
#setup
GPIO.setup(red_led,GPIO.OUT)
GPIO.setup(green_led,GPIO.OUT)
GPIO.setup(red_signal_led,GPIO.OUT)
GPIO.setup(push_button,GPIO.IN,GPIO.PUD_UP)
def time_press(push_button):
    while True:
        if GPIO.input(push_button) == False:
            start_time = time.time()
            while (GPIO.input(push_button))==False:
                   pass
            end_time = time.time()
            interval = end_time - start_time
            return interval #duration of button press 
def green_on(green_led,count):
    publish.single(topic_state,payload="State 1",qos = 0,hostname=hostname,port=port)
    GPIO.output(green_led,1)
    time.sleep(5)
    publish.single(topic_state,payload="State 2",qos = 0,hostname=hostname,port=port)
    for i in range (1,12):
        if  i % 2 == 0:
            GPIO.output(green_led,1)
            time.sleep(0.25)
        else:
            GPIO.output(green_led,0)
            time.sleep(0.25)
        
def activation(interval):
    if interval >= 0.5:
        return True
def red_on(red_led, red_signal_led, count):
    publish.single(topic_state,payload="State 3",qos = 0,hostname=hostname,port=port)
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
        time.sleep((5-difference) + 3)
    elif difference >= 5:
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
            red_on(red_led, red_signal_led,count)      
        count += 1
except KeyboardInterrupt:
    print("CTRL-C: Terminating program.")
finally:
    print("Cleaning up GPIO...")
    GPIO.cleanup()
