from datetime import datetime
import pytz
import time
import requests

IST = pytz.timezone('Asia/Kolkata')


print("script initialized")

while(True):

  datetime_ist = datetime.now(IST)
  if datetime_ist.strftime('%H:%M:%S') == "00:00:00" :
    print("sending invoke")
    r =requests.get('http://gopalakmilk.com/Gopalak_Website/Templates/orange_template/now-ui-dashboard-master/examples/deliveryProcess.php?invoke=vacationReimbursement')
    print(r.status_code)
    time.sleep(100)
  else:
    continue