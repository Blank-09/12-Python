from math import ceil

length = int(input('Enter the length: '))
heigth = ceil(length/2)


for i in range(length):
  for j in range(length):
    if not (j < length - heigth - i or j > length - heigth + i or j > length + heigth - 2 - i or j < i + heigth - length):
      j += 1
    else:
      j = ' '
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