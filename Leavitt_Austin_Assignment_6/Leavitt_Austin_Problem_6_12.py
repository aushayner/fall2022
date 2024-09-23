'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#: 6.
Description: write a function that prints the characters between ch1 and ch2
with the specified number of characters per line

write a test program which prints ten characters per line for 1 to z

'''
#print chars definition
def printChars(ch1, ch2, numberPerLine):

    counter = 1 #counts the character in the line

    #swap characters if character 2 comes first
    if ch2 < ch1:
        ch1, ch2 = ch2, ch1

    current = ch1 #holds the current character

    while current <= ch2:
        print(f"{current}", end = ' ')
        current = chr(ord(current) + 1)
        
        if counter == numberPerLine:
            print()
            counter = 1
        else:
            counter += 1


#main function definition
def main():

    #call printChars function from 1 to Z with 10 per line
    printChars('1', 'Z', 10)


#invoke the main function
main()
        

    
