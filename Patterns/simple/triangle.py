# Using for and operator
for i in range(5):
  for j in range(9):
    if not (j >= 4 - i and j <= 4 + i):
      j = ' '
    print(j, end=' ')
  print()


# Separator 
print('\n') # ignore this line: this line prints two new lines
# Separator


# Using for or operator
for i in range(5):
  for j in range(9):
    if (j < 4 - i or j > 4 + i):
      j = ' '
    print(j, end=' ')
  print()


# Output of both the above programs
'''
OUTPUT:
        4
      3 4 5       
    2 3 4 5 6     
  1 2 3 4 5 6 7   
0 1 2 3 4 5 6 7 8


        4
      3 4 5       
    2 3 4 5 6     
  1 2 3 4 5 6 7   
0 1 2 3 4 5 6 7 8
'''