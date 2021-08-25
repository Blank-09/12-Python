'''
  Write a program that finds sum of all even numbers in a list.
'''

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# You can also write [n+1 for n in range(10)] or 
# range(1,11)

# Using for loop
total = int()

for num in lst:
  if num % 2 == 0:
    total += num

print(total)

# Advance method
# total = sum(((num if (num%2==0) else 0) for num in lst))
total = sum([num if num%2==0 else 0 for num in lst])
print(total)