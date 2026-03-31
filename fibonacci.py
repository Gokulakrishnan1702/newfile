n = int(input("Enter the number of terms: "))
a, b = 0, 1
for _ in range(n):
    print(a)
    a, b = b, a + b