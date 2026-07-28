"""
Character Counter: Write a Python program that:

Asks the user for a string.
Prints how many characters are in the string, excluding spaces.

"""
sent=input("Enter a sentence to count it's length: ")
print("Length of the input sentence = ", len(sent))

sent1=sent.replace(" ","")
print("Length of the input sentence(Without Whitespaces)=",len(sent1))
