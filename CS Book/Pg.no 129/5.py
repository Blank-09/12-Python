'''
  Write a program to create a mirror image of the given string.
'''

# Using Slicing method
string = input("Enter String: ")
reverse = string[::-1]
print(string+'|'+reverse)

# Using while loop
string = input("Enter String: ")
reverse = ""
index = 1

while index <= len(string):
  reverse += string[-index]
  index += 1

print(string+'|'+reverse)

# Using for loop
string = input("Enter String: ")
reverse = ""

for i in range(len(string)-1, -1, -1):
  reverse += string[i]

print(string+'|'+reverse)