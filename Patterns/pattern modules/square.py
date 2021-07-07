from rectangle import Rectangle

class Square (Rectangle):
  def __init__(self, length):
    self.width = self.height = length

  def __str__(self):
    return f'Square(side={self.width})'

  def set_height(self, height):
    self.width = self.height = height