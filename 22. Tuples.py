"""
A Tuple is a collection of items that is ordered and immutable (unchangeable)

Tuples are similar to lists but once a tuple is created you cannot modify it
They are often used to group related data together

"""

#Syntax - my_tuple=(element1,2,3,...)

tuple=("apple","chikoo","banana")
num_tuple=(2,3,1,4,2,6)

#Creating a tuple with one element

single_tuple=("pineapple")

#You can access tuples using indexing just like lists. They also support negative indexing 

print(tuple)
print(num_tuple)
print(tuple[0])
print(tuple[:2])
print(num_tuple[0:5:2])