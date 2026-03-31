
numbers = [12, 45, 2, 41, 31, 10, 99, 4]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("The largest number is:", largest)