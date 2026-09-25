#   3. Write a Python program to append, delete and display elements of a list.

courses = []

courses.append("Artificial Intelligence")
courses.append("Computer Networks")
courses.append("Advanced Database Systems")

print("Before deleting items from list:")
print(courses)

courses.remove("Advanced Database Systems")

print("After deleting items from list:")
print(courses)

