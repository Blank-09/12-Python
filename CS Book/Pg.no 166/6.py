'''
  Write a program to insert a value in a list at the specified location
'''

# list of numbers
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Specified location (sl)
sl = 5

# Specified value (sv)
sv = 21

# using .insert() method
lst.insert(sl, sv)

print(lst)


# without using .insert() method

def insert(lst, index, value):
  # left part (lp)
  lp = lst[:index]

  # right part (rp)
  rp = lst[index+1:]

  # clearing list
  lst.clear()

  # appending items line by line
  # for item in [lp, [value], rp]:
  #   # lst.extend(item)
  #   lst += item

  # Other methods
  # lst.extend([*lp, value, *rp])
  lst.extend(lp + [value] + rp)

  print(lst)

insert(lst, sl, sv)

# slicing method
lst[sl:sl] = [sv]
print(lst)