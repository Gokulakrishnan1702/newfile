a= int(input())
    if a not in [3, 5]:
        print("Invalid input")
    else:
        for i in range(1, 101):
            if i % a == 0:
                print(i)