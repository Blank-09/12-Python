from math import ceil

length = int(input('Enter the base length of the triangle: '))
height = ceil(length/2)

for i in range(5):
  for j in range(9):
    if j >= (height -1 - i) and j <= (height -1 + i): j += 1
    else:
      j = ' '
    print(j, end=" ")
  print()

'''
OUTPUT:
Enter the base length of the triangle: 9
        4
      3 4 5       
    2 3 4 5 6     
  1 2 3 4 5 6 7   
0 1 2 3 4 5 6 7 8
'''