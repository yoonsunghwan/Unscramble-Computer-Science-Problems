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
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

outgoing_calls = []
incoming_calls = []
outgoing_texts = []
incoming_texts = []

#outgoing_calls
for call in calls:
    outgoing_calls.append(call[0])


#incoming_calls
for call in calls:
    incoming_calls.append(call[1])

#outgoing_texts
for text in texts:
    outgoing_texts.append(text[0])

#incoming_texts
for text in texts:
    incoming_texts.append(text[1])

#unique calls and texts
outgoing_ucalls = list(set(outgoing_calls))
incoming_ucalls = list(set(incoming_calls))
outgoing_utexts = list(set(outgoing_texts))
incoming_utexts = list(set(incoming_texts))

#all calls by telemarketers
telemarketers = []
for ucalls in outgoing_ucalls:
    if ucalls not in incoming_ucalls:
        telemarketers.append(ucalls)
    if ucalls not in outgoing_utexts:
        telemarketers.append(ucalls)
    if ucalls not in incoming_utexts:
        telemarketers.append(ucalls)

#unique telemarketers numbers
utelemarketers = list(set(telemarketers))

#print task
print("These numbers could be telemarketers: ")
print(*sorted(utelemarketers), sep = '\n')
