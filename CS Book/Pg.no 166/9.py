'''
  Write a program that counts the numbers of times a value appears in the list. Using a loop to do the same
'''

lst = ['a', 'b', 'c', 'd', 'a', 'a', 'd']

# Using .count() method
for i in lst:
  print(f"'{i}' appeared: {lst.count(i)} time(s)")

# print('='*23)

# Using sets() with .count()
lst2 = list(set(lst))

for i in lst2:
  print(f"'{i}' appeared: {lst.count(i)} time(s)")


# Using dictionaries
count = dict()

for i in lst:
  if i in count:
    count[i] += 1
  else:
    count[i] = 1

  # count[i] = count.get(i, 0) + 1

print(count)
