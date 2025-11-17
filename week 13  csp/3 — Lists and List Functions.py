# # Objective:
# # Students will understand how to create, modify, and access elements in Python lists.

# # Topics Covered:
# # Creating lists, indexing, slicing, appending, popping, sorting, reversing.

# # Examples:

# my_list = ['apple', 'banana', 'cherry']
# print(my_list[0])         # apple
# print(my_list[1:])        # ['banana', 'cherry']

# my_list.append('grape')
# print(my_list)

# my_list.pop(1)
# print(my_list)

# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)

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

list_of_items= list(range(1,1001))
print(list_of_items)
print(len(list_of_items)) 
list_of_items.extend(range(1001,2001))
print(len(list_of_items))


                    
# # Create a list with 5 of your favorite foods.s
# # Print the second and last item.

# # Add a new item using .append().

# # Remove the first item using .pop(0).

# # Reverse your list using .reverse().

# # Create a list of 3 lists (matrix), and access the middle element.