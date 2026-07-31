#Although Tuples are immutable, you can perform various operations with them 

#Tuple Concatenation 

t1=(1,2,3)
t2=(4,5,6)
t3=t1+t2

print(t3) #prints (1,2,3,4,5,6)
print(t3[0:4])

#Tuple Repetition : You can repeat a tuple multiple times using * Operator 

repeat_tuple=(1,2,3)*4
print(repeat_tuple)

