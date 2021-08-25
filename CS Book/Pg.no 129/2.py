'''
    Write a program to count the occurrences of each word in a given string.
'''

# Using Python Dictionary

words = input('Enter a string: ').split()
count = dict()

# normal method
for word in words:
  if word in count:
    count[word] += 1
  else:
    count[word] = 1

# Using get method
for word in words:
  count[word] = count.get(word, 0) + 1

print(count)
# End of program

# If you want to diplay it in a neat format then
for word, count in count.items():
  print(word + ":", count)