employees = ["Ali", "Sara", "Ahmed", "Zain"]

working_hours = {
    "Ali": 45,
    "Sara": 38,
    "Ahmed": 42,
    "Zain": 50
}

completes_tasks = {
    "Ali": True,
    "Sara": True,
    "Ahmed": False,
    "Zain": True
}

def Employee(x):
    return x in employees

def WorksMoreThan40Hours(x):
    return working_hours[x] > 40

def CompletesTasks(x):
    return completes_tasks[x]

def BonusEligible(x):
    return (
        Employee(x)
        and WorksMoreThan40Hours(x)
        and CompletesTasks(x)
    )

for x in employees:
    if BonusEligible(x):
        print(x, "is eligible for a performance bonus.")
    else:
        print(x, "is not eligible for a performance bonus.")

result = any(BonusEligible(x) for x in employees)

print("Does an eligible employee exist?", result)