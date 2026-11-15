rooms = {
    "Living Room": {"person_present": True, "temperature": 32},
    "Bedroom": {"person_present": False, "temperature": 34},
    "Kitchen": {"person_present": True, "temperature": 28}
}

def Room(x):
    return x in rooms

def PersonPresent(x):
    return rooms[x]["person_present"]

def TemperatureAbove30(x):
    return rooms[x]["temperature"] > 30

def ACOn(x):
    return (
        Room(x)
        and PersonPresent(x)
        and TemperatureAbove30(x)
    )

for x in rooms:
    if ACOn(x):
        print(x, ": Turn AC ON")
    else:
        print(x, ": Keep AC OFF")