'''
  Write a program that prints the maximum value in a Tuple
'''

tup = (1, 2, 3, 5, 10, 2, 5)

# Using max function
maximum = max(tup)
print(maximum)

# using for loop
largest = tup[0]

for num in tup:
  if largest < num:
    largest = num

print(largest)
