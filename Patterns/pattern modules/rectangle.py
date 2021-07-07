class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    self.area = self.width*self.height
    return self.area

  def get_perimeter(self):
    self.perimeter = 2 * (self.width + self.height)
    return self.perimeter
  
  def get_diagonal(self):
    self.diagonal = (self.width ** 2 + self.height ** 2) ** .5
    return self.diagonal

  def get_picture(self):
    self.picture = ''
    for i in range(self.height):
      for j in range(self.width):
        self.picture += '* '
      self.picture += '\n'
    return self.picture
  
  def draw(self, times=1, space=0):
    self.img = ''
    s = ''
    for i in range(space):
      s += ' '
    for i in self.get_picture().split('\n'):
      self.img += (i+s)*times + '\n'
    return self.img

  def get_amount_inside(self, other):
    return (self.height * self.width) // (other.width * other.height)

  def set_side(self, size):
    self.width = self.height = size

# a = Rectangle(10, 5)
# print(a.draw(2, 1))