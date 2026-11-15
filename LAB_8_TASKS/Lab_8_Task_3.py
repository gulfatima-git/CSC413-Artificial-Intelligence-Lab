students = ["Ali", "Sara", "Ahmed", "Fatima"]

completes_modules = {
    "Ali": True,
    "Sara": True,
    "Ahmed": False,
    "Fatima": True
}

passes_exam = {
    "Ali": True,
    "Sara": False,
    "Ahmed": True,
    "Fatima": True
}

def Student(x):
    return x in students

def CompletesModules(x):
    return completes_modules[x]

def PassesExam(x):
    return passes_exam[x]

def Certificate(x):
    return (
        Student(x)
        and CompletesModules(x)
        and PassesExam(x)
    )

for x in students:
    if Certificate(x):
        print(x, "is eligible for a course completion certificate.")

result = any(Certificate(x) for x in students)

print("Does an eligible student exist?", result)