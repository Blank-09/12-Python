from triangle import Triangle

class Rhombus(Triangle):
  def __init__(self, length):
    super().__init__(length)

  def __str__(self) -> str:
      return f'Rhombus(width: {self.base//2})'

  def get_picture(self) -> str:
    self.picture = str()

    for i in range(self.base):
      for j in range(self.base):
        if (j < self.base - self.height - i or j > self.base - self.height + i or j > self.base + self.height - 2 - i or j < i + self.height - self.base):
           self.picture += self.blank
        else:
          self.picture += self.symbol
        self.picture += self.space
      self.picture += '\n'

    return self.picture

# a = Rhombus(9)
# print(a.draw(8)*2)
# print(a.get_picture())



# a = Rhombus(9)
# a.set_symbols('A')



# print(a.draw())
# print(a.draw(5))
# print(a.draw(5, 10))
# a.set_symbols('O')
# a.set_baseLength(3)
# print(a.draw())


'''
        😎
      😎😎😎
    😎😎😎😎😎
  😎😎😎😎😎😎😎
😎😎😎😎😎😎😎😎😎
  😎😎😎😎😎😎😎
    😎😎😎😎😎
      😎😎😎
        😎
'''