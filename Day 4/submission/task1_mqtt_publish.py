import paho.mqtt.publish as publish

hostname = "test.mosquitto.org" #Sandbox broker
port = 1883 #default port for unencrypted MQTT

topic = "Fernando_MQTT/test" #'/' is used as the delimiter for sub-topics

publish.single(topic,payload = "Hello,EEE Student!", qos = 0,
            hostname = hostname,
            port = port)