def encode(message):
    count = 0
    word  = message[0]
    string =""
    for char in message:
        if word == char:
            count +=1
        else:
            string += str(count) + word
            count = 1
            word = char
    
    string += str(count) + word
    return string



#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)