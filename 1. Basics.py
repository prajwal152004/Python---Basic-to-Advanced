name="Prajwal"
sname=" Dragneel"
age=20  #variable age is assigned the value 20
weight=70 
age_float=float(age) # Type conversion. Variable age is made to convert it's value from integer to float and assigned to variable age_float
weight_float=float(weight) # Type conversion. Variable weight is made to convert it's value from integer to float and assigned to variable weight_float
student= False

print(age_float+weight_float)
print(age+weight)

s="100"
print(age+int(s)) # Used type conversion (Only because s was 100. It wouldn't have converted if it was a letter)
print(student)
print(type(student))
print(type(s))
print(type(age_float))
print(type(age))