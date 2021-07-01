from math import ceil

length = int(input('Enter the base length of the triangle: '))
height = ceil(length/2)

for i in range(height):
  for j in range(length):
    if (j < height -1 - i or j > height -1 + i):
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