__author__ = "Priyanshu"
'''
  Write a program to count the number of characters, words and lines in a given string.
'''

# We can use .readlines() but we want it as a string not as a list
# By considerding string point of view
string = open('Pg.no 129\sample.txt').read()
lines = string.split('\n')
empty = ""

count = {
  'characters': 0,
  'words': 0,
  'lines': len(lines),
}

for line in lines:
  if line is empty:
    continue

  words = line.split()
  count['words'] += len(words)

  for word in words:
    count['characters'] += len(word)
      
print(count)

# Another method
count = {
  'characters': sum([sum([len(word) for word in line.split()]) for line in lines]),
  'words': sum([len(word.split()) for word in lines]),
  'lines': len(lines),
}

print(count)


# after Shortening variable name
a = lines

count = {
  'characters': sum([sum([len(c) for c in b.split()]) for b in a]),
  'words': sum([len(b.split()) for b in a]),
  'lines': len(a),
}

print(count)

# Without dict()
# s = open('Pg.no 129\sample.txt').read()
# a = s.split('\n')

print('Characters:', sum([sum([len(c) for c in b.split()]) for b in a]))
print('Words:', sum([len(b.split()) for b in a]))
print('Lines:', len(a))