a=[1,2,3,4,5]
print(len(a))

#pop()
print(a.pop())
#append()
a.append(7)
print(a)

a = [14,5,6,3,6,9]
a.sort()
print(a)
#sort in reverse order  
a.sort(reverse=Tru
    e)
    print(a)
    # Print numbers between 1 and 100 divisible by 3 or 5 only
    cycle = int(input())
    if cycle not in [3, 5]:
        print("Invalid input")
    else:
        for i in range(1, 101):
            if i % cycle == 0:
                print(i)