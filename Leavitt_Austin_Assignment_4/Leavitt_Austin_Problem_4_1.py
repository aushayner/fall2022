'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment 4/ Problem# 4.1:
Description: Solve quadratic equations

NOTE: the math.sqrt() function will throw a math domain error if it has
a negative value

'''

#Prompt the user to enter three values for a, b, c

a,b,c = eval(input("Enter a, b, c:"))

#Store the discriminant value into a variable

discriminant = b * b - 4 * a * c

#Multi-way if statement to check the discriminant cases

if discriminant < 0:
    print("The equation has no real roots")
elif discriminant == 0:
    r1 = -b / (2 * a)
    print(f"The root is {int(r1)}")
else:
    #Discriminant > 0
    r1 = (-b + discriminant ** 0.5) / (2 * a)
    r2 = (-b - discriminant ** 0.5) / (2 * a)
    print(f"The roots are {r1:.6f} and {r2:.6f}")
