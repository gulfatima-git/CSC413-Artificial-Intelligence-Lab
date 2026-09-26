#   1. Create functions to calculate the mean, maximum and minimum of a list 
#      without using built-in max(), min() or sum().

def calculate_mean(num):
    sum = 0
    
    for i in num:
        sum+= i

    return sum/len(num)

def calculate_min(num):
    min = num[0]

    for i in num:
        if i < min:
            min = i

    return min

def calculate_max(num):
    max = num[0]

    for i in num:
        if i > max:
            max = i

    return max

num = []

for i in range(5):
    n = int(input("Enter a number: "))
    num.append(n)

print(f"The mean of the list is: {calculate_mean(num)}")
print(f"The minimum element of the list is: {calculate_min(num)}")
print(f"The maximum element of the list is: {calculate_max(num)}")