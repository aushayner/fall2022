'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#: 6.35
Description:
Use the functions in random character to generate 10,000 uppercase letter
and count the occurences of A
'''
#import the random character functions
from RandomCharacter import getRandomUpperCase

aCount = 0 #count the occurences of 'A'

for i in range(10000):
    ch = getRandomUpperCase()
    if ch == 'A':
        aCount += 1


print(f"A occured {aCount} times out of 10,000")


