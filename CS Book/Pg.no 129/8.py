'''
  Write a program to swap two strings.
'''

str1 = "World"
str2 = "Hello"

# Using multiple assignment
print("Before:", str1, str2)
str2, str1 = str1, str2
print("After :",str1, str2)

# Without double assignment
print("Before:", str1, str2)
temp = str1
str1 = str2
str2 = temp
print("After :",str1, str2)