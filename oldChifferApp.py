import string
import random

#Function to generate a random key 

def generateKey():
    alphabet = list(string.ascii_uppercase)
    random.shuffle(alphabet)
    return {string.ascii_uppercase[i]: alphabet[i] for i in range(26)}


# Function to encrypt a text using a given key

def encrypt(text, key): 
    encryptedText = ''
    for char in text:
        if char.upper() in key: 
            if char.isupper():
                encryptedText += key[char.upper()].upper()
            else: 
                encryptedText += key[char.upper()].lower()
        else:
            encryptedText += char
    return encryptedText

# Function to decipher a text using a given key

def decipher(text, key):
    reversedKey = {value: key for key, value in key.items()}
    decipheredText = ""
    for char in text:
        if char.upper() in reversedKey:
            if char.isupper():
                decipheredText += reversedKey[char.upper()].upper()
            else:
                decipheredText += reversedKey[char.upper()].lower()
        else:
            decipheredText += char
    return decipheredText

# Testkode
originalText = "Hei, Verden!"
    
key = generateKey()
    
encryptedText = encrypt(originalText, key)
print("Encrypted text:", encryptedText)
    

decipheredText = decipher(encryptedText, key)
print("Decrypted text:", decipheredText)
    
# sammenlign tekstene
if originalText == decipheredText:
    print("Koden er knekt!")
else:
    print("Koden er ikke knekt.")