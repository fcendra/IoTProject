from datetime import datetime
import time
from sense_hat import SenseHat 
import logging

f = open("record.txt","w+")
sense = SenseHat()
sense.clear()

for i in range (1,50):
    today = datetime.now()
    temp = sense.get_temperature()
    tempRounded = round(temp,2)
    time.sleep(1)
    print(today, tempRounded)
    f.write(str(today)+" "+str(tempRounded)+"\r\n")  
f.close()