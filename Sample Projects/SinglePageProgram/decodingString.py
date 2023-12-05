inputString=input("Enter the Input String:- ")
caesarCipher=int(input("Enter the Caesar Cipher number to shift the Number:- "))

def decodeString(num, string):
    decodedString=""
    for i in string:
        asciiNum=ord(i)
        decodedString+= chr(asciiNum-num)
    
    return decodedString

print(decodeString(caesarCipher, inputString))