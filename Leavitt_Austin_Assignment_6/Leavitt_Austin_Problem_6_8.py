'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#: 6.8
Description: write a module that contains functions for converting from
celsius to fahrenheit and fahrenheit to celsius. Write a test program to
show conversion results in a table

'''
#function for conversion celsius to fahrenheit
def celsiusToFahrenheit(celsius):
    return (9 / 5) * celsius + 32

#function for conversion fahrenheit to celsius
def fahrenheitToCelsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

#main function definition for displaying a table of conversions
def main():
    #display header
    print(f"{'Celsius':15}{'Fahrenheit':10}{'|':^3}{'Fahrenheit':15}{'Celsius':15}")

    #display table body
    for i in range(10):
        print(f"{(40 - i):<15.1f}{celsiusToFahrenheit(40 - i):<10.1f}{'|':^3}{(120 - (i * 10)):<15.1f}{fahrenheitToCelsius(120 - (i * 10)):<15.2f}")


#invoke the main function
main()
