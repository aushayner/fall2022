'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#: 6.5
Description: write a function to display three numbers in increasing order.
Write a test program that allows the user to enter three numbers and
display them in increasing order
'''
#function for displaying 3 numbers in increasing order
def displaySortedNumbers(num1, num2, num3):

    #if num1 is greater than num2 swap them
    if num1 > num2:
        num1, num2 = num2, num1

    #if num2 is greater than num3 swap them
    if num2 > num3:
        num2, num3 = num3, num2

    #if num1 is greater than num2 swap them
    if num1 > num2:
        num1, num2 = num2, num1

    print(f"{num1} {num2} {num3}")

#main function definition
#get input for the three numbers from the user
def main():

    #get 3 numbers from user
    num1, num2, num3 = eval(input("Enter three numbers: "))

    #invoke the displaySortedNumbers function
    displaySortedNumbers(num1, num2, num3)


#invoke the main function
main()
    


