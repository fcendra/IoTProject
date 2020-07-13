import paho.mqtt.publish as publish

hostname = "test.mosquitto.org" #Sandbox broker

port = 1883

topic_state = "PC000/traffic_light/emergency"

question = input("What is the emergency status: ")

#if-else statement
if question == "Normal":
    publish.single(topic_state,payload=False,qos = 0,hostname=hostname,port=port)
elif question == "Emergency":
    publish.single(topic_state,payload=True,qos = 0,hostname=hostname,port=port)
