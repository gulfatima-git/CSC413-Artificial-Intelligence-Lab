#   Build a student-record program using a dictionary. Add, update, search and delete student records.

studentrecord = {
    "name": "Gul",
    "DOB": "2004-11-19"
}

print(studentrecord)

studentrecord["age"] = 22

print(studentrecord)

studentrecord.update({"name": "Gul Fatima"})
print(studentrecord)

x = studentrecord["name"]
print(x)

studentrecord.pop("age")
print(studentrecord)