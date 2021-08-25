'''
  Write a program that creates a list of numbers from 1 to 50 that are either divisible by 3 or divisible by 6
'''

# we know the fact that the hcf of 3 and 6 is 3
# and also 3 is a prime number where as 6 is not
# Then we can conclude that every multiple of 3 is divisible by 3
# And every 3 multiples multiplied by 2 is divisible by 6

index = 3
lst = list()

while index <= 50:
  lst.append(index)
  index += 3

print(lst)

# Using for loop
lst = list()

for i in  range(1, 51):
  if i%3 == 0:
    lst.append(i)

print(lst)

# Using filter() function
print(list(filter(lambda n: n%3 is 0, range(1,50))))
# this type of chaining of function is known as function chaining
