

#Opening the message from a text file and moving it into a string called message
with open('message.txt','r') as file:
    message = file.read()

#Transfer table to swap characters in the string and print the new message.
transTable = message.maketrans("mq'rgszpdjeohxlukc-,w .it;vao\"byfn", " theandlousofyricbmvpgk,.x;-'w\"zjq")
message = message.translate(transTable)
print(message)