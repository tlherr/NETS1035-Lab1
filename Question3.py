# Thomas Herr
# 200325519
# NETS1035 Applied Cryptography

# 3.	Create a jumble program using indexing
# a.	Take a string and create substrings
# b.	Move the strings to create a jumbled string
# c.	Print out the jumbled string
# d.	Advanced: Make the substrings random

import random

input = input("Enter a string to jumble: ")
substrings = list()
inputsize = len(input)
combinedstring = ''

for x in range(0, inputsize-1):
    substrings.append(input[x:random.randint(x,inputsize-1)])

for substring in substrings:
    combinedstring+=substring

print(combinedstring, sep=' ')