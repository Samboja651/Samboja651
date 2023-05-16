"""
File: ecyption & decryption.py
Encrypt and input string of lowercase letters and prints
the result. The other input is the distance value.
"""

plainText = input("Enter a one-word, lowercase message: ")
distance = int(input("Enter the distance value: "))
code = " "
for ch in plainText:
    ordValue = ord(ch)
    #print("Plain Value",ordValue)
    cipherValue = ordValue + distance
    #print("Cipher value",cipherValue)
    #print(ord('a'))
    if cipherValue > ord('z'):
        cipherValue = ord('a') + distance - \
                      (ord('z') - ordValue + 1)
        #print("new cipher value",cipherValue)
    code += chr(cipherValue)
print("Ecypted message is",code)

# decrypt cipher text
for ch in code:
    ordValue = ord(ch)
    cipherValue = ordValue - distance
    if cipherValue < ord('a'):
        cipherValue = ord('z') - \
                      (distance - (ord('a') - ordValue + 1))
        plainText += chr(cipherValue)
#print("Decrypted message is",plainText)
