"""
Logical Operator Practice: Write a Python program that takes two numbers as input from the user and checks if:

Both numbers are greater than 10 (using and).
At least one of the numbers is less than 5 (using or).
The first number is not greater than the second (using not).

"""

print("Is a > b ? ")
a=int(input("Input a = "))
b=int(input("Input b = "))
print(a)
print(b)

print("Is a and b greater than 10 ? :", a > 10 and b > 10)
print("Is one of the numbers is less than 5 : ", a<5 or b<5)
print(" The first number is not greater than the second ", not(a>b))


"""
Comparison Operator Challenge: Create a Python program that asks the user for their age and prints:

"You are an adult" if the age is greater than or equal to 18.
"You are a minor" if the age is less than 18.
Use >= and < comparison operators.

"""

age=int(input("Enter your age : "))
print(age)

print(f"It's {age>=18} that you're an adult ")
print(f"It's {age<18} that you're a minor")

"""
Membership Operator Exercise: Write a Python program that:

Takes a string as input from the user.
Checks if the letter 'a' is in the string (using in).
Checks if the string doesn't contain the word "Python" (using not in).

"""

string= input("Input a string ")
print("Does the string has a in it ?","a" in string)
print("Does the string has Python in it ( Output is True - if it's not there | False - if it's there)?","Python" not in string )


"""
Bitwise Operator Task: Given two integers, write a Python program that:

Prints the result of a & b, a | b, and a ^ b.
Shifts the bits of a two positions to the left (a << 2).
Shifts the bits of b one position to the right (b >> 1).

"""

a=int(input("Input a : "))
b=int(input("Input b : "))
print("Bitwise Operation of a&b gives the result as : ",a&b)
print("Bitwise Operation of a|b gives the result as : ",a|b)
print("Bitwise Operation of a^b gives the result as : ",a^b)
print("Bitwise Operation of a<<2 gives the result as : ",a<<2)
print("Bitwise Operation of b>>1 gives the result as : ",b>>1)