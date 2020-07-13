import paho.mqtt.client as mqtt

hostname = "test.mosquitto.org" #Sandbox broker

port = 1883 #Default port for unencrypted MQTT

topic_state= "PC000/#" #Wildcard character '#' indicates all sub-topics
            #(e.g.PC000/test,PC000/sensor/temperature,etc.)

def on_connect(client, userdata,flags,rc):
    #Successful connection is '0'
    print("[MQTT] Connection result: "+str(rc))
    if rc == 0:
        #Subscribe to topics
        mqttc.subscribe(topic_state)

def on_publish(mqttc,userdata,mid):
    print("[MQTT] Sent: " +str(mid))

def on_disconnect(mqttc,userdata,rc):
    if rc != 0:
        print("Disconnected unexpectedly")

def on_message(mqttc,userdata,message):
    print("Received message on %s: %s (QoS = %s)" %
          (message.topic,message.payload.decode("utf-8"),
           str(message.qos)))

mqttc = mqtt.Client()
mqttc.on_publish = on_publish
mqttc.on_message = on_message
mqttc.on_disconnect = on_disconnect
mqttc.on_connect = on_connect
mqttc.connect(hostname, port = port,keepalive=60,bind_address="")
mqttc.loop_forever()
