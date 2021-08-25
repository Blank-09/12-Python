'''
  Write a program to create a list of numbers in the range 1 to 20. Then delete all the numbers from the list that are divisible by 3
'''

# creates a list of 1 to 20
lst = list(range(1,21))

# deleting number which are divisible by 3 from the list
# Using .remove() method
for i in lst:
  if i%3 == 0:
    lst.remove(i)

print(lst)

# Using filter
lst = range(1,21)
print(list(filter(lambda n: n%3 != 0, lst)))
