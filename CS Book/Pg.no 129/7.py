'''
  Write a program to append a string to another string without using += operator
'''

str1 = input("Enter String: ")
str2 = input("Enter Another String: ")

# Using concatination '+' method
x,y = str1,str2
x = x+y
print(x)

# Using list and join() method
x,y = str1,str2
x = "".join([x,y])
print(x)
