'''
  Write a program to remove duplicates from a list.
'''

myList = ['a', 'b', 'c', 'd', 'a', 'a', 'd']

# Using set() function
print(set(myList))

# Normal Method
def removeDuplicates(lst):
  temp = lst.copy() 
  lst.clear()

  for item in temp:
    if item not in lst:
      lst.append(item)


removeDuplicates(myList)
print(myList)
