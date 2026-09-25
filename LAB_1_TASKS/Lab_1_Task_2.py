#   2. Write a Python program that takes a number between 1–12 from the user and returns the month name. 
#      Use Python match-case.

num = int(input("Enter a number between 1 to 12: "))

def check_number(num):
    match num:
        case 1:
            return "January"
        case 2:
            return "February"
        case 3:
            return "March"
        case 4:
            return "April"
        case 5:
            return "May"
        case 6:
            return "June"
        case 7:
            return "July"
        case 8:
            return "August"
        case 9:
            return "September"
        case 10:
            return "October"
        case 11:
            return "November"
        case 12:
            return "December"
        case _:
            return "Invalid Month!"

print(check_number(num))