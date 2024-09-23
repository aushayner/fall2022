'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#: 6.4
Description: Write a function to display an integer in reversed order.
Write a test program to which prompt the user to enter an integer to reverse.

'''

#reverse number function
def reverse(number):
    #variable for storing the reversed number
    newNumber = 0

    #reverse the number using mod and integer division
    while number % 10 > 0:
        newNumber *= 10
        newNumber += number % 10
        number //= 10

    #return the reversed number
    return newNumber

#main function
def main():

    #get the integer from the user
    number = eval(input("Enter an integer: "))

    #display the reversed number
    print(f"{number} reversed is {reverse(number)}")


#invoke the main function
main()
    

