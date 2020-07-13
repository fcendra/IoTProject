from sense_hat import SenseHat
sense = senseHat()
sense.clear()

pressure = sense.get_pressure()
temp = sense.get_temperature()
tempRounded = round(temp,2)
humidity = sense.get_humidity()

while True:
    for event in sense.stick.get.events():
        if event.action == 'pressed':
            print(tempRounded)