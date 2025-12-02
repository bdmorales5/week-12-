# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.

# Examples:

my_list = ['apple', 'banana', 'cherry']
print(my_list[0])         # apple
print(my_list[1:])        # ['banana', 'cherry']

my_list.append('grape')
print(my_list)

my_list.pop(1)
print(my_list)

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)

#collects are used to store multiple items in a single variable
# list are ordered collections of items
# list are mutable, meaning you can change their
# # Practice Problems:
list_of_fruits=["apple","banana","cherry","date"]
print(list_of_fruits) 
print(type(list_of_fruits))
# Accessing items in a list
print(list_of_fruits[0]) 
print(list_of_fruits[1])
print(list_of_fruits[-1])
print(list_of_fruits[1:3])
# reversing a list 2 ways
list_of_fruits.reverse()
print(list_of_fruits)
print(list_of_fruits[::-1]) 
list_of_fruits.append("elderberry")
print(list_of_fruits)
list_of_fruits.extend(["mango", "dragon fruit", "grape"])
print(list_of_fruits[0]) 
print(list_of_fruits[1])
print(list_of_fruits[-1])

list_of_fruits.reverse()
print(list_of_fruits)
print(list_of_fruits[::-1]) 

# popping item from list
popped_item=list_of_fruits.pop()
print(popped_item)
print(list_of_fruits)
# inserting item at a specific index
list_of_fruits.insert(1,"blueberry")
print(list_of_fruits)
# removing a specific item by value
list_of_fruits.remove("banana")
print(list_of_fruits)
list_of_fruits.insert(3, "banana")
list_of_fruits.sort()# sorts the list in ascending order
print(list_of_fruits)
# why use list instead of individual variable

list_of_items= list(range(1,100000000001))
print(list_of_items)
print(len(list_of_items)) 
list_of_items.extend(range(1001,2001))
print(len(list_of_items))


#   # Make a list of 5 foods
# foods = ["pizza", "burger", "pasta", "tacos", "sushi"]

# Print the second and last food
print(foods[1])
print(foods[-1])

# Add a new food
foods.append("ice cream")

# Remove the first food
foods.pop(0)

# Reverse the list
foods.reverse()

# Make a small matrix and print the middle number
matrix = [
    [1, 2, 3],
    [4, 5, 6],  # middle row
    [7, 8, 9]
]

print(matrix[1][1])  # middle element
# instead pf creating separate variables
# for each item we can store them in a list
# this makes our job easier
# this makes managing the complexity of our code easier
# when we need to manage multiple items


# set and tuples
# set and tuples are also part of collections
# fa,ily in python
set1= {1,2,3,4,5}
set2={1,2,3,4,5}
print(set1)
print(set2)
print(type(set1))
set_with_duplaction={1,2,3,4,4,5}
print(set_with_duplaction)
print(3 in set1)
print(6 in set1)


tuple1=(1,2,3,4,5)
tuples2=('apple','banana','cherry')

print(tuple1)
print(tuples2)
print(type(tuple1))

social_security_number = (123444,4444445,5676789)