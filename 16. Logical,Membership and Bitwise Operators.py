"""
LOGICAL OPERATORS

Logical operators are used to combine conditional statements
They evaluate expressions and return either True or False

and : Returns TRUE if both conditions are True
or  : Returns TRUE if one of the conditions are True 
not : Reverses the logic state of it's operand (True becomes False, False becomes True)

"""

x=5
y=10
z=15
print("Performing operations on the data x=5, y=10, z=15")
print("The Output for x>0 and y>5 : ",x>0 and y>5) #Prints TRUE (Since both conditions are true)
print("The Output for x>10 or z>10  : ",x>10 or z>10) #Prints TRUE (Since one condition is true)
print("The Output for not(x>10) : ",not(x>10)) #Prints TRUE (Reverses FALSE to True)
print("  ")

"""
MEMBERSHIP OPERATORS

Membership operators test for membership within a sequence such as list,string or tuple
They return True or False based on whether the value is found in the sequence

in     : Returns TRUE if specified value is found in the sequence
not in : Returns TRUE if specified value is not found in the sequence

"""

my_list= [1,2,3,4,5]
my_string= "Python"


print("The output for 3 in my_list : ", 3 in my_list)
print("The output for z in my_string : ", "z" in my_string)
print("The output for z not in my_string : ", "z" not in my_string)
print("The output for 6 in my_list : ",6 in my_list)
print("  ")

"""
BITWISE OPERATORS

Perform operations on binary representations of integer. 
These operators are useful for low level programming tasks like working with bits and bytes

&  : Bitwise AND (sets each bit to 1 if both bits are 1).
|  : Bitwise OR (sets each bit to 1 if one of the bits is 1).
^  : Bitwise XOR (sets each bit to 1 if only one of the bits is 1).
~  : Bitwise NOT (inverts all the bits).
<< : Left shift (shifts bits to the left by a specified number of positions).
>> : Right shift (shifts bits to the right by a specified number of positions).

"""
a=5 #In Binary 101
b=3 #In Binary 011

print("The output for a=5 (In Binary 101) and b=3 (In Binary 011) is below")
print("The output for a&b : ",a&b)
print("The output for a|b : ",a|b)
print("The output for a^b : ",a^b)
print("The output for ~a : ",~a)
print("The output for a<<1 : ",a<<1)
print("The output for a>>1 : ", a>>1)