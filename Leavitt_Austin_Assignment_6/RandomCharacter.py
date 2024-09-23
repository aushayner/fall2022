'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#:
Description: Will have 5 functions that randomly generate specific types
of characters

'''
#import randint
from random import randint

#generate a random character between ch1 and ch2
def getRandomCharacter(ch1, ch2):

    return chr(randint(ord(ch1), ord(ch2)))

#generate a random lowercase letter
def getRandomLowerCase():
    #invoke getRandom character
    return getRandomCharacter('a', 'z')

#generate a random upper case letter
def getRandomUpperCase():
    #invoke getRandomCharacter function
    return getRandomCharacter('A', 'Z')

#generate a random digit character
def getRandomDigit():
    #invoke random character function
    return getRandomCharacter('0', '9')

#generate a random ascii character
def getRandomASCIICharacter():
    return chr(randint(0,127))
    
