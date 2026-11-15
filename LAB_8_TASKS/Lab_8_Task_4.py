passengers = ["Ali", "Sara", "Ahmed", "Zain"]

seats_available = {
    "Ali": True,
    "Sara": True,
    "Ahmed": False,
    "Zain": True
}

sufficient_balance = {
    "Ali": True,
    "Sara": False,
    "Ahmed": True,
    "Zain": True
}

def Passenger(x):
    return x in passengers

def SeatsAvailable(x):
    return seats_available[x]

def SufficientBalance(x):
    return sufficient_balance[x]

def CanBook(x):
    return (
        Passenger(x)
        and SeatsAvailable(x)
        and SufficientBalance(x)
    )

for x in passengers:
    if CanBook(x):
        print(x, "can book a ticket.")
    else:
        print(x, "cannot book a ticket.")

result = any(CanBook(x) for x in passengers)

print("Does a passenger exist who can book a ticket?", result)