'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment 4/ Problem# 4.5:
Description: Find future dates. Receive a date and its day in the week and
days elapsed into the future then output the date and day of the week
of the new day

'''
#Prompt the user to enter an integer for today
today = eval(input("Enter today's day: "))
elapsedDays = eval(input("Enter the number of days elapsed since today: "))

#Calculate the future day
futureDay = (today + elapsedDays) % 7

#Multi-Way if statement to convert today value into the string day value
if today == 0:
    nameToday = "Sunday"
elif today == 1:
    nameToday = "Monday"
elif today = 2:
    nameToday = "Tuesday"
elif today = 3:
    nameToday = "Wednesday"
elif today = 4:
    nameToday = "Thursday"
elif today = 5:
    nameToday = "Friday"
else:
    nameToday = "Saturday"

#Multi-Way if statement to convert futureDay value into the string day value
if futureDay == 0:
    nameFuture = "Sunday"
elif futureDay == 1:
    nameFuture = "Monday"
elif futureDay = 2:
    nameFuture = "Tuesday"
elif futureDay = 3:
    nameFuture = "Wednesday"
elif futureDay = 4:
    nameToday = "Thursday"
elif futureDay = 5:
    nameFuture = "Friday"
else:
    nameFuture = "Saturday"

#Output the result
print(f"Today is {nameToday} and the future day is {nameFuture}")
