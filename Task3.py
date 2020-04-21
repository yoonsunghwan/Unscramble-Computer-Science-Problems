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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.
"""

fixed_lines = []
mobile_numbers = []
telemarketers = []

def get_fixed_lines(calls):
    for call in calls:
        if call[0][0] == '(':
            fixed_lines.append(call[0])
        elif call[1][0] == '(':
            fixed_lines.append(call[1])
def get_mobile_numbers(calls):
    for call in calls:
        if call[0][0] in ['7','8','9'] and ' ' in call[0]:
            mobile_numbers.append(call[0])
        elif call[1][0] in ['7','8','9'] and ' ' in call[0]:
            mobile_numbers.append(call[1])
def get_telemarketers(calls):
    for call in calls:
        if call[0][0:3] == '140':
            telemarketers.append(call[0])
        elif call[1][0:3] == '140':
            telemarketers.append(call[1])
#section the different numbers accordingly
get_fixed_lines(calls)
get_mobile_numbers(calls)
get_telemarketers(calls)

#get all the numbers that have the bangalore codes in fixed_lines
bangalore_numbers = []
bangalore_code = '(080)'
for numbers in fixed_lines:
    if numbers.startswith(bangalore_code):
        bangalore_numbers.append(numbers)
    

#get unique bangalore numbers by putting into set and turning back to list
unique_bangalore_numbers = list(set(bangalore_numbers))

#removed (080) from the numbers
code_removed = []
for n in unique_bangalore_numbers:
    code_removed.append(n[5:])

unique_bangalore_inorder = sorted(code_removed)
print("The numbers called by people in Bangalore have codes:")
print(*unique_bangalore_inorder, sep ='\n')

"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
#number of calls where a person in bangalore calls another person in bangalore
num_of_bangalore_out_in = 0
for call in calls:
    if call[0].startswith(bangalore_code) and call[1].startswith(bangalore_code):
        num_of_bangalore_out_in +=1
#number of calls made in bangalore 
bangalore_calls_out = 0
for call in calls:
    if call[0].startswith(bangalore_code):
        bangalore_calls_out += 1
        
percent = (num_of_bangalore_out_in / bangalore_calls_out) * 100
print("{:.2f}% percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percent))
      
