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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in \
lexicographic order with no duplicates.
"""
sending_texts = set([text[0] for text in texts])
receiving_texts = set([text[1] for text in texts])

outgoing = set([call[0] for call in calls])
incoming = set([call[1] for call in calls])


telemarketers = []

for call_sender in outgoing:
    if (call_sender not in incoming and call_sender not in
       receiving_texts and call_sender not in receiving_texts):
        telemarketers.append(call_sender)

telemarketers.sort()

print("\n These numbers could be telemarketers:")
for possible_telemarketers in telemarketers:
    print(possible_telemarketers)
