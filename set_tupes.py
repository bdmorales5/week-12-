# sets and tuples example
# set example
set1 = {1,2,3,4,5}
print(set1)
print(type(set1))
set1.add(6)
print(set1)
set1.remove(2)
print(set1)


# set drop duplicate items
set2 = {"apple", "banana", "cherry", "cherry"}
print(set2) #{"apple", "banana", "cherry", "cherry"}

# tuples example
tuple1=(1,2,3,4,5)
print(tuple1) #(1,2,3,4,5)
print(type(tuple1))

# tuples are immutable, meaning they cannot be changed after creation
# this makes tuples useful for storing data that should not be modified

social_security_number = (123444, 444445, 5676768)
print(social_security_number) #(123444, 444445, 5676768)