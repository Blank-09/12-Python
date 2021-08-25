'Write a python program to find the length of a string.'

# Simplest method (Single line)
string = input("Enter something: ")
lengthOfString = len(string)
print(lengthOfString)


'''
    Without using len()
'''

# Using for loop (3 lines)
string = input("Enter something: ")
lengthOfString = int()

for i in string:
  lengthOfString += 1

print(lengthOfString)