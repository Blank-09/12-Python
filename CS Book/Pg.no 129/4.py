'''
  Write a program to print integers with '*' on the right of specified width
'''

integer = int(input('Enter integer: '))
width = int(input('Enter width: '))
print('Original value:', integer)
print(f'Formatted number with right padding of width {width}): '+'{:*<{}d}'.format(integer, width))


# Another method without using .format()
integer = input('Enter integer: ')
width = int(input('Enter width: '))
print('Original value:', integer)

length = len(integer)

if length < width:
  print(integer + '*'*(width - length))
else:
  print(integer)

print(integer + '' if length >= width else '*'*(width-length))