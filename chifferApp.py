import random
import string
import nltk
from collections import Counter
from nltk.corpus import words

# Encrypted text
encryptedText = "Xzm blf xizxp gsrh evib xlnkovc xlwv? Ru hl blf'iv lm gsv irtsg gizxp!"

# Lookup table for letter frequency in English
lookupTableLetterFrequency = {
    'e': 12.702, 't': 9.056, 'a': 8.167, 'o': 7.507, 'i': 6.966,
    'n': 6.749, 's': 6.327, 'h': 6.094, 'r': 5.987, 'd': 4.253,
    'l': 4.025, 'c': 2.782, 'u': 2.758, 'm': 2.406, 'w': 2.360,
    'f': 2.228, 'g': 2.015, 'y': 1.974, 'p': 1.929, 'b': 1.492,
    'v': 0.978, 'k': 0.772, 'j': 0.153, 'x': 0.150, 'q': 0.095,
    'z': 0.074
}

# Common English words set
common_words = set(words.words())

def decryptWithFrequencyAnalysis(text):
    letterCount = Counter(char for char in text.lower() if char.isalpha())
    # print("letterCount: ", letterCount)
    
    # Sorter bokstaver etter frekvens i kryptert tekst
    sortedEncryptedLetters = [char for char, _ in letterCount.most_common()]
    # print("sortedEncryptedLetters: ", sortedEncryptedLetters)
    
    # Sorter bokstaver etter frekvens i lookup table
    sortedLookupLetters = [char for char, _ in sorted(lookupTableLetterFrequency.items(), key=lambda item: item[1], reverse=True)]
    random.shuffle(sortedLookupLetters)
    # print("sortedLookupLetters: ", sortedLookupLetters)

    # lag erstatningsnokkel
    letterSubstitution = {enc: dec for enc, dec in zip(sortedEncryptedLetters, sortedLookupLetters)}
    # print("letterSubstitution: ", letterSubstitution)
    
    # Dekrypter basert pa antatt erstatningsnokkel
    decryptedText = ''.join(letterSubstitution[char.lower()] if char.lower() in letterSubstitution else char for char in text)
    
    return decryptedText

def evaluateDecryption(text):
    words = text.split()
    recognized_words = [word for word in words if word.lower() in common_words]
    return len(recognized_words) / len(words) > 0.5  # om over 50% av ordene i teksten er ord i common_words vil det returnere true

# Dekrypter inne i feedback-loop.
attempts = 10000
for attempt in range(attempts):
    decryptedText = decryptWithFrequencyAnalysis(encryptedText)
    print(f'Attempt {attempt + 1}:', decryptedText)
    if evaluateDecryption(decryptedText):
        print("Decryption looks correct!")
        break
    user_feedback = input("Press Enter to try again or type 'stop' to end: ")
    if user_feedback.lower() == 'stop':
        print("Decryption process stopped by user.")
        break
else:
    if attempt == attempts - 1:
        print("Failed to decrypt correctly after several attempts.")
