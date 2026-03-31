# List of common list functions/methods in Python

# 1. append() - Adds an element to the end of the list
my_list = [1, 2, 3]
my_list.append(4)  # [1, 2, 3, 4]

# 2. insert() - Inserts an element at a specific position
my_list.insert(1, 10)  # [1, 10, 2, 3, 4]

# 3. extend() - Adds all elements of an iterable to the end
my_list.extend([5, 6])  # [1, 10, 2, 3, 4, 5, 6]

# 4. remove() - Removes the first occurrence of a value
my_list.remove(10)  # [1, 2, 3, 4, 5, 6]

# 5. pop() - Removes and returns element at given index (default last)
my_list.pop()  # returns 6, list is now [1, 2, 3, 4, 5]

# 6. clear() - Removes all elements
my_list.clear()  # []

# 7. index() - Returns the index of the first occurrence of a value
my_list = [1, 2, 3, 2]
idx = my_list.index(2)  # 1

# 8. count() - Returns the number of occurrences of a value
count = my_list.count(2)  # 2

# 9. sort() - Sorts the list in place
my_list.sort()  # [1, 2, 2, 3]

# 10. reverse() - Reverses the list in place
my_list.reverse()  # [3, 2, 2, 1]

# 11. copy() - Returns a shallow copy of the list
new_list = my_list.copy()

# List modification by assignment
my_list[0] = 100  # [100, 2, 2, 1]

# List slicing
sub_list = my_list[1:3]  # [2, 2]