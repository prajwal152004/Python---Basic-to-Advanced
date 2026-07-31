#Index method - Returns the index value of the specified element 

list=["Apple", "Orange", "Banana", "Chikoo"]
print(list)

print(list.index("Orange")) #Prints the index value of the specified element i.e 1
print(list.index("Chikoo")) #Prints 3

#Count Element - Returns the number of occurances of a specified element in a list 

lists=["Apple", "Orange", "Banana", "Chikoo","Apple", "Apple"]
print(lists.count("Apple")) #Counts how many times apple has occured in the list 

num = [2,3,4,1,4,1,4,5,5,5,5,5,5]
print(num.count(1))
print(num.count(5))

#Reverse - Reverses the elements of the list in place 

list.reverse()  #The list doesn't stay original after using reversing 
print(list)

lists.reverse()
print(lists)

num.reverse()
print(num)

#Sort - Sorts the list in place (Ascending by default)

num.sort()
print(num)


#Nested lists - List can contain other lists, allowing you to create nested lists 
#This can be useful for storing matrix like data structure 

matrix=[
    [2,3,4],
    [5,6,1],
    [0,7,9] 
]

print(matrix[0]) #Use single dimensional if you wanna retrieve a row 
print(matrix[0][2]) #Use two dimensions if you wanna retrieve a specific element in a row