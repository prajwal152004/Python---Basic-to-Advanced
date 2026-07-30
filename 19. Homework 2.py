"""
List Manipulation Exercise:

1. Create a list of 5 items (strings or numbers).
Add a new item to the end of the list and another at the second position.
Remove the third item from the list.
Print the list after each operation.

"""
items=["rock","paper","scissors","salt","chips"]
print(items)

items.append("Chocolate") #Add a new item to the end of the list
print(items)

items.insert(1,"Water") #Add a new item at second position
print(items)

items.pop(2) #remove item from 3rd position (Index 2)
print(items)

items.reverse() #reversing the items
print(items)

"""
2. Reverse and Sort a List: Create a list of numbers and:
Sort it in descending order.
Reverse the sorted list and print it.

"""
numbers=[4,2,1,3,5,6,7]

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)