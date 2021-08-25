__author__ = "Priyanshu"

'''
  Write a program that finds sum of all the numbers in a Tuple using while loop.
'''

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Using while loop
total = int()
index = 0

while index < len(tup):
  total += tup[index]
  index += 1

print(total)

# Using for loop
total = int()
for num in tup:
  total += num

print(total)

# Using sum() method
total = sum(tup)
print(total)