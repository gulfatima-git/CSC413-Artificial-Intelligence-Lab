members = ["Ali", "Sara", "Ahmed", "Fatima"]

borrowed = {
    "Ali": True,
    "Sara": True,
    "Ahmed": False,
    "Fatima": True
}

returned_on_time = {
    "Ali": True,
    "Sara": False,
    "Ahmed": False,
    "Fatima": True
}

def Member(x):
    return x in members

def Borrowed(x):
    return borrowed[x]

def ReturnedOnTime(x):
    return returned_on_time[x]

def CheckMember(x):
    return not Borrowed(x) or ReturnedOnTime(x)

for x in members:
    if Borrowed(x) and not ReturnedOnTime(x):
        print(x, "has not returned the book on time.")
    elif Borrowed(x):
        print(x, "returned the book on time.")

result = all(CheckMember(x) for x in members)

print("Have all members followed the return rule?", result)