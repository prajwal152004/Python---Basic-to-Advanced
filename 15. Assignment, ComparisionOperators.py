#None Operator

x= None  # None = Nothing 
print(x) # Prints None
print(type(x)) #Prints the type of x which is NoneType 

'''
Assignment Operator 

Used to assign values to variables
=  : Assigns value on right to variable left
+= : Adds right operand to left operand and assigns the result to left operand
-= : Subtracts right operand from left operand and assigns the result to left operand
*= : Multiplies left operand by right operand and assigns the result to left operand
/= : Divides the left operand by the right operand and assigns the result to the left operand
%= : Takes modulus 

'''

x=5    #Assigns x as 5
x+=3   # 5+3 = 8, new x = 8
x-=2   # 8-2=6, new x=6
x*=4   # 6*4 = 24, new x=24
x/=6   # 24/6= 4, New x = 4.0

print(x) #Prints x=4.0
print(int(x)) # 4.0 is a floating type. So I converted it to int to print only 4

'''
Comparision Operators

Compares two values. They either return true or false depending on the condition

== : Checks if two values are equal.
!= : Checks if two values are not equal.
>  : Checks if the left operand is greater than the right operand.
<  : Checks if the left operand is less than the right operand.
>= : Checks if the left operand is greater than or equal to the right operand.
<= : Checks if the left operand is less than or equal to the right operand.

'''

a = 10
b=20

print("The answers for comparision operators are (a=10, b=20)")
print("a==b : ",a==b)
print("a!=b : ",a!=b)
print("a>b : ", a>b)
print("a<b : ",a<b)
print("a>=10 : ",a>=10)
print("b<10 : ",b<10)