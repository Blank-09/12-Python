'''
  Write a program to add a prefix text to all the lines in a string.
'''

# The below line of code is for getting the lines of string
fileName = input('Enter file name: ')
try:
  file = open(fileName)
except:
  print('Invalid file name!\nTry again...')
  quit()

# Main program starts from here
prefix = input('Enter prefix: ')

for line in file.readlines():
  print(prefix, line.rstrip())

# Another way

multiLineString = '''
Lorem ipsum dolor sit amet consectetur adipisicing elit.
Fugiat quidem dignissimos voluptates exercitationem dicta.
hic minima quaerat error cupiditate voluptate mollitia aspernatur,
non natus perspiciatis voluptas quod nemo laboriosam nesciunt.
'''

prefix = input('Enter prefix: ')
empty = ''

for line in multiLineString.split('\n'):
  if line is not empty:
    print(prefix, line)
