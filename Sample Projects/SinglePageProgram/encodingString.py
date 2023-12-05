inputString=input("Enter the Input String:- ")
caesarCipher=int(input("Enter the Caesar Cipher number to shift the Number:- "))

def encodeString(num, string):
    encodedString=""
    for i in string:
        asciiNum=ord(i)
        encodedString+= chr(asciiNum+num)
    
    return encodedString

print(encodeString(caesarCipher, inputString))