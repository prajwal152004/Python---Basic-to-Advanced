boy_name=input("Boy's Name: ")
boy_age= int(input("Boy's Age: "))
girl_name=input("Girl's Name: ")
girl_age=int(input("Girl's Age: "))

print(f"{boy_name} is {boy_age} years old and {girl_name} is {girl_age} years old.")
# Easier way of concatinating string where every variable is converted to string and concatenated
print(boy_name + " is " + str(boy_age) + " years old and " + girl_name + " is " + str(girl_age) + " years old " )
# A bit complex way of concatinating string with easier arithmetic operation
print(boy_name + " loves " + girl_name + " and their age difference is " + str(abs(boy_age - girl_age)))
# Same as the above used absolute function for the absolute value of ages because sometimes the boy's age might be lesser than the girl's age
