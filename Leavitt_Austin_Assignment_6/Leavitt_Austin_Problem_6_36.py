'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#: 6.
Description: use the functions is RandomCharacter to print 100 upper case
letters and then 100 single digits, printing 10 per line

'''
#import RandomCharacter module
from RandomCharacter import *

#print 100 uppercase letters
for i in range(1, 101):
    print(f"{getRandomUpperCase()}", end = ' ')

    if i % 10 == 0:
        print()

#print 100 single digits
for i in range(1, 101):
    print(f"{getRandomDigit()}", end = ' ')

    if i % 10 == 0:
        print()
