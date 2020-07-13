import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt

hostname = "test.mosquitto.org"

port = 1883

userdata = None
message = None
topic_state = "PC000/traffic_light/emergency"

def on_connect(client, userdata,flags,rc):
    #Successful connection is '0'
    print("[MQTT] Connection result: "+str(rc))
    if rc == 0:
        #Subscribe to topics
        mqttc.subscribe(topic_state)

def on_publish(mqttc,userdata,mid):
    print("[MQTT] Sent: " +str(mid))
    return mid

def on_disconnect(mqttc,userdata,rc):
    if rc != 0:
        print("Disconnected unexpectedly")

def on_message(mqttc,userdata,message):
    print("Received message on %s: %s (QoS = %s)" %
          (message.topic,message.payload.decode("utf-8"),
           str(message.qos)))
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

mqttc = mqtt.Client()
mqttc.on_publish = on_publish
mqttc.on_message = on_message
mqttc.on_disconnect = on_disconnect
mqttc.on_connect = on_connect
mqttc.connect(hostname, port = port,keepalive=60,bind_address="")          

try:
    while True:
        payload = mqttc.on_publish#Find variable that contains payload
        mqttc.loop_start()
        while payload == False:
            if count % 2 == 0:
                GPIO.output(red_led,0)
                GPIO.output(red_signal_led,0)
                green_on(green_led,count) 
            else:
                GPIO.output(green_led,0)
                red_on(red_led, red_signal_led,count)      
            count += 1
        while payload == True:
            GPIO.output(red_led,0)
            GPIO.output(green_led,0)
            GPIO.output(red_signal_led,1)
            time.sleep(0.25)
            GPIO.output(red_signal_led,0)
            time.sleep(0.25)
except KeyboardInterrupt:
    print("CTRL-C: Terminating program.")
finally:
    print("Cleaning up GPIO...")
    GPIO.cleanup()

