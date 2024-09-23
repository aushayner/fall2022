'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#:
Description: Display n x n matrix

'''

#import random module
import random

def main():
    #Prompt the user to enter n
    n = eval(input("Enter n: "))

    #Invoke the printMatrix function
    printMatrix(n)


#Create the printMatrix function
def printMatrix(n):

    #nested for loop
    for i in range(n):
        for j in range(n):
            print(random.randint(0, 1), end = " ")

        #Jump to new line
        print()


#Invoke the main function
main()


