from square import Square
from rectangle import Rectangle
from triangle import Triangle
from rhombus import Rhombus

class Shapes:
  def __init__(self) -> None:
    self.square = Square(4)
    self.rectangle = Rectangle(10,5)
    self.triangle = Triangle(9)
    self.rhombus = Rhombus(9)

a = Shapes()
print(a.rectangle.draw())

# rect = Rectangle(10, 5)
# print(rect.get_area())
# rect.set_height(3)
# print(rect.get_perimeter())
# print(rect)
# print(rect.get_picture())

# sq = Square(9)
# print(sq.get_area())
# sq.set_side(4)
# print(sq.get_diagonal())
# print(sq)
# print(sq.get_picture())

# rect.set_height(8)
# rect.set_width(16)
# print(rect.get_amount_inside(sq))