# Using and operator
for i in range(9):
  for j in range(9):
    if not (j < (13  - i) and j >= (i - 4) and j >= (4 - i) and j <= (4 + i)):
      j = ' '
    print(j, end=' ')
  print()


# Separator 
print('\n') # ignore this line: this line prints two new lines
# Separator


# Using or operator
for i in range(9):
  for j in range(9):
    if (j < 4 - i or j >= 5 + i or j >= 13 - i or j < i - 4):
      j = ' '
    print(j, end=" ")
  print()


'''
OUTPUT:
          4
        3 4 5
      2 3 4 5 6
    1 2 3 4 5 6 7
  0 1 2 3 4 5 6 7 8
    1 2 3 4 5 6 7
      2 3 4 5 6
        3 4 5
          4


          4
        3 4 5
      2 3 4 5 6
    1 2 3 4 5 6 7
  0 1 2 3 4 5 6 7 8
    1 2 3 4 5 6 7
      2 3 4 5 6
        3 4 5
          4
'''