'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#: 6.1
Description: Write a function to get a pentagonal number, n(3n-1)/2,
use function to display the first 100 pentagonal numbers with 10
numbers on each line

'''

#function which returns the pentagonal number of n
def getPentagonalNumber(n):

    return n * (3*n -1) / 2

#main function which utilizes the getPentagonalNumber function
#to display the first 100 pentagonal function
def main():

    #for loop 1-100
    for i in range(1, 101):
        print(f"{int(getPentagonalNumber(i))}", end = ' ')

        #print a newline after 10 numbers
        if i % 10 == 0:
            print()
    
#invoke the main function
main()
