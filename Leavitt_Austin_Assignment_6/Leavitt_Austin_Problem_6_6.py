'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#: 6.6
Description: Write a function to display a pattern to the nth row.
Write a test program which allows the user to enter a value for n.

'''

#displayPattern function definition
def displayPattern(n):

    #nested for loops for printing the pattern
    #rows
    for i in range(1, n+1):
        #columns
        for j in range(0, n - i):
            print(" ", end = " ")

        for j in range(i, 0, -1):
            print(f"{j}", end = " ")

        print()


#main function definition
def main():

    n = eval(input("Enter a number: "))

    displayPattern(n)

#invoke the main function
main()
