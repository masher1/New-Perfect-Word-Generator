import enchant
import random

dictionary = enchant.Dict('en-US')

def newWordGenerator():
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    newWord = ""
    newWordlen = 0
    randNum = 0

    while (newWordlen < 100):
        if 100-newWordlen >= 26 or newWordlen == 0 or newWordlen == 1:
            randNum = 25
        else:
            randNum = 100 - newWordlen
        newChar = random.randrange(0, randNum)
        while(newChar + newWordlen >= 100):
            newChar = random.randrange(0, randNum)
        newWordlen += newChar+1
        newWord += alphabet[newChar]
    return newWord

wordsList = []
sample = open('output.txt', 'w')
while 1:
    word = newWordGenerator()
    if dictionary.check(word):
        if word not in wordsList:
            wordsList.append(word)
            print("Is", word, "a real word? ", dictionary.check(word), file=sample)

sample.close()