
"""secquence type
mutable type - can change the values
bro has atributes
a[5]
a=[1,2,3,4,5,5]
"""
""""
a=[1,2,3,4,5,5]
print(a)
print(type(a))
a[2]=100
print(a)


#slicing

print(a[0:2])
print(a[:4])
print(a[3:])


""

# find the type of lists
a=[1,"Harini",'A',0.5,[1,2,3,4,5]]
print(a)
a.append(7) # adding element

print(a)

"""

'''
print(type(a))
print(a[0]," this type is: " ,type(a[0]))
print(a[2]," this type is: " ,type(a[2]))
print(a[1]," this type is: " ,type(a[1]))
print(a[4]," this type is: " ,type(a[4]))
print(a[3]," this type is: " ,type(a[3]))
print(a[4][1])
'''
'''
a=[1,2,3,4,5]
print(a)
#a.clear()

b=a.copy()
print("b:",b)
print("---------------------")
print(a.count(5)) 

print("Index: ",a.index(5)) 

print(len(a))
print("---------------------------------------------------------------------------------")
print(max(a))
print(min(a))
'''

list1=["hi","we","are"]
for i in list1:
    print(list1[i]), 
