'''
  Write a program that reverse a list using a loop.
'''

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using while loop
reverse = list()
index = -1

while index >= -len(lst):
  reverse.append(lst[index])
  index -= 1
print(reverse)

# Using for loop
reverse = list()
for i in range(len(lst)-1, -1, -1):
  reverse.append(lst[i])

print(reverse)

# Using slicing method
reverse = lst[::-1]
print(reverse)

# Using reversed() function
reverse = reversed(lst)
print(list(reverse))