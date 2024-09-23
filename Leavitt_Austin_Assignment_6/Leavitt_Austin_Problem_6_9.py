'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#: 6.
Description: write a module that contains functions for converting from
foot to meter and meter to foot. Write a test program to
show conversion results in a table

'''
#function for conversion meters to feet
def meterToFoot(meter):
    return meter / 0.305

#function for conversion feet to meters
def footToMeter(foot):
    return 0.305 * foot

#main function definition for displaying a table of conversions
def main():
    #display header
    print(f"{'Feet':10}{'Meters':10}{'|':^3}{'Meters':10}{'Feet':10}")

    #display table body
    for i in range(0, 10):
        print(f"{(i+1):<10.1f}{footToMeter(i+1):<10.3f}{'|':^3}{(20 + 6 * i):<10.1f}{meterToFoot(14 + 6 * i):<10.3f}")


#invoke the main function
main()
