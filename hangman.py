import random
from words import words
import string

def getWord():
    return random.choice(words)

def display(x,l):
    d={}
    for i in range(len(x)):
        d[i] = x[i]

    for i in l:
        if i in d:
            d.pop(i)

    for i in range(len(x)):
        if i in d:
            print(d[i],end=" ")
        else:
            print("_",end=" ")

    print("")

def ind(d,a):
    for i in d:
        if d[i]==a:
            return i

def hangman(x,l):
    
    word = dict()
    for i in l:
        word[i] = x[i].upper()
    alpha = set(string.ascii_uppercase)
    usedLetter = set()

    while True:
        display(x,l)

        print("previous incorrect guesses: ",end="")
        for i in usedLetter:
            print(f"{i} ",end='')
        print("")

        userLetter = input("Make a guess: ").upper()
        
        if userLetter in alpha:
            if userLetter in list(word.values()):
                l.remove(ind(word,userLetter))
                word.pop(ind(word,userLetter))
                print("You have Guessed Correctly\n")
            else:
                usedLetter.add(userLetter)
                print("Incorrect guess. Try again\n")
        else:
            print("Enter a valid character\n")

        if len(word) == 0:
            print("you have guessed the complete word:-")
            display(x,[])
            break



x = getWord()
l= list(range(len(x)))


print(x+"\n"*15)
hangman(x,random.choices(l,k=len(x)//2 +1))
