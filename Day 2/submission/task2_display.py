from sense_hat import SenseHat
sense = SenseHat()

blue = (0,0,255)
yellow = (255,255,0)
red = (255,0,0)
white = (255,255,255)
green = (0,255,0)
indigo = (0,28,200)
orange = (255,165,0)
violet = (238,130,238)

listOfSequences = [[red,white],[orange,red],[yellow,orange],[green,yellow],[blue,green],[indigo,blue],[violet,indigo]]

while True:
  counter = 0
  if counter != 7:
    for i in range (0,7):
      sense.show_message("EEE is awesome!", text_colour=listOfSequences[i][0], back_colour=listOfSequences[i][1], scroll_speed=0.05)
      counter += 1
    else:
      counter = 0

