# # List methods


# Python has a set of built-in methods that you can use on lists/arrays.

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

#append()

fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)

#clear()

fruits = ['apple', 'banana', 'cherry', 'orange']

fruits.clear()

print(fruits)

#copy

fruits = ['apple', 'banana', 'cherry', 'orange']

x = fruits.copy()
print(fruits)

#count

points = [1, 4, 2, 9, 7, 8, 9, 3, 1]

x = points.count(9)

print (points)

#extend

fruits = ['apple', 'banana', 'cherry']

points = (1, 4, 5, 9)

fruits.extend(points)

print(fruits)
print(points)

#insert

fruits = ['apple', 'banana', 'cherry']
fruits.insert(2,"Guava")
print(fruits)