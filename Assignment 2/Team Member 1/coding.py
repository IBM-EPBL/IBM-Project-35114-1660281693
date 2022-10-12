import random
import time

while(1):
  temp = random.randint(0,100)
  humidity = random.randint(0,100)
  if temp>60:
     print("ALERT!" Detected temperature:" + str(temp))
     time.sleep(1)