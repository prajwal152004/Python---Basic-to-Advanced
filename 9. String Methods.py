message = " Hello Guys ! "

print(message.upper()) # This convers all the letters to uppercase letters
print(message.lower()) # The same way this converts all letters to lowercase letters
print(message.strip()) # This removes the leading and trailing whitespaces/blankspaces in the message string and prints out
print(message.replace("Hello", "Hi")) #This replaces a specific value in a string with other string you needed to replace

#The below method is one type of writing a string with inverted commas
new = "Praj says 'Hello'"
print(new)

#The above one was only if you needed a single inverted commas within your string and the below methods to be used if you need double inverted commas within your strings
hey = 'Praj says "Hello"'
print(hey)

# Below to be used if you want to use multi line strings without any problems
yo = '''Praj says hi
        Luffy says hi '''
print(yo)

# Let's now try to learn the length of strings each whitespace and all characters are counted 
a= "let's now print a message"
print(len(a))

b= "Prajwal" #Here index values are [ Index P=0, r=1, a=2, j=3, w=4, a=5, l=6]
             #[Position P= 1, r=2, a=3, j=4, w=5, a=6, l=7]

print(b[0]) # This prints only P from the string
print(b[1])
print(b[2])
print(b[3])
print(b[-1]) #-1=l, -2=a...etc represents the strings from last 
print(b[-2])

# you can also extract a portion of substring using slicing method

print(b[0:5])
print(b[2:6]) #String slices from index 2 to position 6
print(b[:6]) #Prints from starting point to 6th position(not index)
print(b[5:]) #Prints from 5th index to next full string
print(b[:]) #Prints every string

#Remember the formula [Start Index : End Position : Step/Skip]
#If you want to Print all string skipping one letter after other You can use the below method
print(b[1::3]) # This prints rw where r has the index 1 and skips to 3rd position and prints w