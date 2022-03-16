
#Importing collections so that Counter can be used to count each character in the message.
import collections
from collections import Counter

#Opening the message from a text file and moving it into a string called message
with open('message.txt','r') as file:
    message = file.read()

#Calling Counter and storing result in 'c'
c = Counter(message)

#Printing the message
print(c)

