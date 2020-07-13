from sense_hat import SenseHat
from itertools import permutations
sense = SenseHat()

blue = (0,0,255)
yellow = (255,255,0)
red = (255,0,0)
white = (255,255,255)
green = (0,255,0)
indigo = (0,28,200)
orange = (255,165,0)
violet = (238,130,238)

listOfColors = [blue,yellow,red,white,green,violet,orange,indigo]
listOfSequence = list(permutations(listOfColors,2))

while True:
  for i in range(len(listOfSequence)):
    sense.show_message("EEE is awesome!", text_colour=listOfSequence[i][0],back_colour=listOfSequence[i][1],scroll_speed=0.05)