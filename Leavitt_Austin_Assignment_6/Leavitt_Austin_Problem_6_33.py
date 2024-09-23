'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#: 6.33
Description: Rewrite exercise 3.4 using a function to returnt he area of
a pentagon

'''
#import the math library for use of tan and pi
import math

#define the area function
def area(s):
    return (5 * (s ** 2)) / (4 * math.tan(math.pi / 5))

#define the main function to get user input
def main():

    #prompt user for the side length
    s = eval(input("Enter the side: "))

    print(f"The area of the pentagon is {area(s)}")

#invoke the main function
main()
    
    
