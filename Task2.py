"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
from datetime import datetime

length = 0


for c in calls:
    if int(c[-1]) > length:

        duration = int(c[-1])
        tel_number = c[0]
        date = c[-2]

        length = duration
        
#make date a datetime object
d = datetime.strptime(date, '%d-%m-%Y %H:%M:%S')
#create new variable month_year to match Month Name and Year format
month_year = d.strftime('%B %Y')

print(f'{tel_number} spent the longest time {duration} seconds, on the phone during {month_year}.')


