'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#: 6.34
Description: rewrite problem 3.5 to use a function
to calculate the area of a regular polygon

'''
#import the math function
import math

#define the area function
def area(n, side):
    return (n * (side ** 2)) / \
       (4 * math.tan(math.pi / n))

#define the main function to receive the number of sides and side
#length from the user
def main():

    n = eval(input("Enter the number of sides: "))
    side = eval(input("Enter the side length: "))

    print(f"The area of the polygon is {area(n, side)}")

#invoke the main function
main()

    
