#Enter the message
#split the words into the characters 
# get the ascii value of each character and increment the value by 5
# convert the ascii values into the string

#splitting the string into the comma seprated words
from fileinput import filename


def stringToList(string):
    message_arr = string.split()
    return message_arr

#Encrypted data will be stored into this enc_data
enc_data = []

# message_char will store the comma seprated charaters of each word
message_char = []

# Outer loop will iterate all the words from the list message_arr
def wordToChar(word_list):
    for message in word_list:
        # inner loop will iterate each single character from the iterable variable message of message_arr
        for char in message:
            message_char.append(char)
    return message_char
    
# ascii_val will iterate the list which is containing the list of each character and covert it into the ascii value and store the values in var enc_data
def ConvertCharToAscii(list_to_ascii):
    for ascii_val in list_to_ascii: 
        data = ord(ascii_val)
        enc_data.append(data)
    return enc_data

# This for loop is incrementing the ascii value of list enc_data
def increment(list_of_ascii):
    i = 0
    for increment in list_of_ascii:
        incre_data = increment+5
        enc_data[i] = incre_data
        i+=1
    return enc_data

def decrement(list_of_ascii):
    i=0
    for decrement in list_of_ascii:
        decre_data = decrement-5
        dec_data[i] = decre_data
        i+=1
    return dec_data

# This for loop is converting the each ascii value into the character.
def AsciiToChar(ascii_list):
    i = 0
    for char_con in ascii_list:
        con_data = chr(char_con)
        enc_data[i] = con_data
        i+=1
    return enc_data

# converting the list into string
def listToString(list_string):
    char = ''
    for prevchar in list_string:
        char += '' + prevchar
    return char

# Converting string to ascii
def stringToAscii(string):
    for char in string: 
        data = ord(char)
        dec_data.append(data)
    return dec_data

# saving the content of file on location
def contentOfFile(file,what,string):
    with open(f"E:\\Login data\\{file}.txt",'a') as f:
        f = f.write(f"{what}:{string}")
    print(f"{file}.txt location: E:\\Login data\\{file}.txt ")

# printing enc dec data
def encr_dec_data(encrypted,decrypted):
    print(f"Encrypted data: {encrypted}")
    print(f"Decrypted data: {decrypted}")


print("********** Encoder/Decoder for your text ********** \n")
ed = input("What do you want to do (1)Encoding (2)decoding? (e/d): ")
if ed == 'e' or ed =="E":
    que = input("Do you want to store your data into file? (y/n): ")
message = input("\nEnter your text: ")

message_arr = stringToList(message)
message_char = wordToChar(message_arr)
enc_data = ConvertCharToAscii(message_char)
enc_data = increment(enc_data)
enc_data = AsciiToChar(enc_data)
encrypted_char = listToString(enc_data)

dec_data = []
dec_data = stringToAscii(encrypted_char)
dec_data = decrement(dec_data)
dec_data = AsciiToChar(dec_data)
decrypted_char = listToString(dec_data)

if ed == 'e' or ed == "E":
    if que == 'y' or que ==  'Y':
        print(" ********** Store your data into file **********")
        print("You can store \n(1)Username \n(2)Password \n(3)Any kind of text")
        file_name = input("\nEnter file name: ")
        what_to_store = input("\nWhat do you want to store: ")
        contentOfFile(file_name,what_to_store,encrypted_char)
    else: 
        encr_dec_data(encrypted_char,decrypted_char)
else:
    dec_data = []
    dec_data = stringToAscii(message)
    dec_data = decrement(dec_data)
    dec_data = AsciiToChar(dec_data)
    decrypted_char = listToString(dec_data)
    print(decrypted_char)


    
