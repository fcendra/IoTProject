import threading

###### class definition of myThread #####

class myThread (threading.Thread):

   # define the ID of this thread
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name

   # this threads prints out a message for 3 times
   def run(self):
      for i in range(1, 4):
         print("Running " + self.name + " " + str(i))
      print("Exiting " + self.name)

########## end of myThread ###########

# Create new threads
thread1 = myThread(1, "Thread-1")
thread2 = myThread(2, "Thread-2")

# Start new Threads
thread1.start()
thread2.start()
