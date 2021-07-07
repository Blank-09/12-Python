from math import ceil

class Triangle:
  def __init__(self, length) -> None:
    self.set_symbols('*')
    self.set_baseLength(length)

  def __str__(self):
    return f'Triangle(width: {self.base}, height:{self.height})'

  def set_symbols(self,symbol='*',space=' ',blank=' '):
    self.symbol = symbol
    self.space = space
    self.blank = blank

  def set_baseLength(self, length) -> int:
    self.base = length
    self.height = ceil(length/2)

  def get_picture(self):
    self.picture = str()

    for i in range(self.height):
      for j in range(self.base):
        if (j < self.height -1 - i or j > self.height - 1 + i):
          self.picture += self.blank
        else:
          self.picture += self.symbol
        self.picture += self.space
      self.picture += '\n'
    return self.picture

  def draw(self, times=1, space=0, inverse=False):
    self.img = ''
    s = ''
    for i in range(space):
      s += ' '
    
    arr = self.get_picture().split('\n')[::-1] if inverse else self.get_picture().split('\n')

    for i in arr:
      self.img += (i+s)*times + '\n'

    return self.img.rstrip()

# a = Triangle(9)

# print(a.draw(5, 5), end='')
# print(a.draw(times=5, space=5, inverse=True))