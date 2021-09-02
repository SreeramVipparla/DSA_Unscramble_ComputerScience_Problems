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
"<telephone number> spent the longest time,\
<total time> seconds, on the phone during
September 2016.".
"""
no_of_calls = {}

for user, reciever, timestamp, duration in calls:

    if user in no_of_calls:
        no_of_calls[user] = no_of_calls.get(user, 0)+int(duration)

    if reciever in no_of_calls:
        no_of_calls[reciever] += int(duration)
    else:
        no_of_calls[reciever] = int(duration)

Phone, TimeTaken = (max(no_of_calls.items(), key=lambda x: x[1]))
print(' {} spent the longest time, {} seconds, on the phone during September \
2016.'.format(Phone, TimeTaken))
