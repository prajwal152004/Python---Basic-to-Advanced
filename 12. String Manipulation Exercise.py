"""
String Manipulation Exercise: Write a Python program that:

Takes a sentence as input from the user.
Prints the sentence in all uppercase and lowercase.
Replaces all spaces with underscores.
Removes leading and trailing whitespace.

"""
sent1= input("Hey User! Type in a sentence: ")
print(sent1.upper(),sent1.lower(),sent1.strip(),sent1.replace(" ","_"))

print(sent1.upper())
print(sent1.lower())
print(sent1.strip())
print(sent1.replace(" ","_"))