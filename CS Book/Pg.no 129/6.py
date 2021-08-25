'''
  Write a program which removes all the occurrence of a given character in a string.
'''

# Using .replace()
string = input("Enter String: ")
charToRemove = input("Enter character(s) to be removed: ")
removedCharStr = string.replace(charToRemove, '')
print(removedCharStr)

# Using .split()
removedCharStr = "".join(string.split(charToRemove))
print(removedCharStr)

# Using for loop
removedCharStr = str()
for letter in string:
  if letter is not charToRemove:
    removedCharStr += letter

print(removedCharStr)