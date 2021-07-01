from math import floor

length = int(input('Enter the length: '))
height = floor(length/2)

for i in range(length):
  for j in range(length):
    if j < (length + height  - i) and j >= (i + height + 1 - length) and j >= (height - i) and j <= (height + i):
      j += 1
    else: j = " "
    print(j, end=" ")
  print()

# Enter odd number to get a perfect output
'''
OUTPUT:
Enter the length: 5
      3     
    2 3 4
  1 2 3 4 5
    2 3 4
      3
'''