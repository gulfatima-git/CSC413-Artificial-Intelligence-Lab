#   5. Write a function that accepts a list of numbers and returns separate lists of even and odd numbers.

def getNum(num):
    for i in range (5):
        n = int(input("Enter a number: "))
        num.append(n)

    return num

num = []

print(getNum(num))

even = []
odd = []

for i in range(5):
    if num[i] % 2 == 0:
        even.append(num[i])
    else:
        odd.append(num[i])

print(num)
print(even)
print(odd)