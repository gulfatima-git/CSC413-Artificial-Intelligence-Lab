#   1. Write a Python program that takes an integer from the user, determines whether it is positive, 
#      negative or zero, determines whether it is even or odd, and displays a message about each result.

integer = int(input("Enter a number: "))


if integer > 0:
    print(f"{integer} is a positive number.")
elif integer < 0:
    print(f"{integer} is a negative number.")
else:
    print(f"{integer} is neither positive nor negative, it is zero.")

if integer % 2 == 0:
    print(f"{integer} is an even number.")
else:
    print(f"{integer} is an odd number.")
