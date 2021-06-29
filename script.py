from datetime import datetime
import pytz
import time

IST = pytz.timezone('Asia/Kolkata')


print("script initialized")

while(True):

  datetime_ist = datetime.now(IST)
  if datetime_ist.strftime('%H:%M:%S') == "14:30:00" :
    print("yes")
    time.sleep(100)
  else:
    continue