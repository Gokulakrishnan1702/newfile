import array as arr

a = arr.array('i', [])  # create an empty integer array
n = int(input("Enter how many numbers: "))

for i in range(n):
    num = int(input("Enter a number: "))
    a.append(num)

print("Array elements:",a)



      