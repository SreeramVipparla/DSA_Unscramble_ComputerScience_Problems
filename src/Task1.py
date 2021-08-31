"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
no_of_diff_num= set()

for unique_txt in texts:
    no_of_diff_num.add(unique_txt[0])
    no_of_diff_num.add(unique_txt[1])

for unique_calls in calls:
    no_of_diff_num.add(unique_calls[0])
    no_of_diff_num.add(unique_calls[1])

print('There are {} different telephone numbers in the records.'.format(len(no_of_diff_num)))