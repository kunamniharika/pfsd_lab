import datetime
import time

print(time.time())
print(time.asctime())

Niharika = datetime.datetime.now()
print(Niharika)
print("Year:", Niharika.year)
print("Month:", Niharika.month)

import calendar

s = calendar.prcal(2023)
s2 = calendar.month(2005, 4)
s1 = calendar.isleap(2005)
print(s1)

import datetime

x = datetime.datetime.now()
from datetime import timedelta

print(x + timedelta(days=-89))

import time
from datetime import datetime
import pytz

time1 = pytz.timezone('Europe/Berlin')
print("Current Time is :", datetime.now(time1))



