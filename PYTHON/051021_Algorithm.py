
def gcd(a, b):
    while (b != 0):
        t = a
        a = b
        b = t % b 
    return a

print(gcd(20, 8))



for x in range(5, 10):
    if x % 2 == 0:
        continue
    print(x)
            
days = ['mon', 'tue', 'wed', 'thur', 'friday', 'saturday', 'sunday']
for i, d in enumerate(days):
    print(i, d)


import math 

print('The square of root of 16 is', math.sqrt(16))

print('pi is ', math.pi)




today = date.today()
print(today)

print(today.weekday())

today = datetime.now()
print(today)

now = datetime.now()
print(now.strftime('The current year is : %a, %d, %B, %y'))

print(now.strftime('locale date and time: %X'))

from _typeshed import OpenTextMode
from datetime import date
from datetime import time 
from datetime import datetime
from datetime import timedelta

print(timedelta(days=365, hours=5, minutes=1))

now = datetime.now()
print('today is ' + str(now + timedelta(days=365)))

t = datetime.now() - timedelta(weeks=1)

print(t)

today = date.today()
afd = date(today.year, 3, 1)
if afd < today:
    print('april .. %d days ago' % ((today-afd).days))
    afd = afd. replace(year=today.year+1)


import calendar 

c = calendar.TextCalendar(calendar.SUNDAY)
st = c.formatmonth(2021, 1, 0, 0)
print(st)

hc = calendar.HTMLCalendar(calendar.SUNDAY)
st = hc.formatmonth(2021,1)
print(st)

c = calendar.TextCalendar(calendar.SUNDAY)
for i in c.itermonthdays(2017, 8):
    print(i)

import os
from os import path 
import datetime
from datetime import date, time, timedelta
import time


print(os.path)