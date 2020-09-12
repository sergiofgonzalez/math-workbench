#
## Defining classes
#
class Rectangle():
  # constructor
  def __init__(self, w, h):
    self.width = w
    self.height = h

  # regular instance method
  def area(self):
    return self.width * self.height

  # regular instance method with args
  def scale(self, factor):
    return Rectangle(self.width * factor, self.height * factor)

  # special method: equality
  def __eq__(self, other):
    return self.width == other.width and self.height == other.height

  # special method: string representation (aka toString)
  def __repr__(self):
    return 'Rectangle (%r by %r)' % (self.width, self.height)

  # operator overloading when instance comes on the left-hand side, and on the right-hand side
  def __mul__(self, factor):
    return self.scale(factor)

  def __rmul__(self, factor):
    return self.scale(factor)

  # class methods (aka static methods)
  @classmethod
  def square(cls, side):
    return Rectangle(side, side)


r = Rectangle(3, 4)
print(r)
print(type(r))
print("r.width = %d, r.height = %d" % (r.width, r.height))

print("area(r)=%d" % r.area())
print(Rectangle(5, 3).area())

enlarged = r.scale(2)
print("enlarged.width = %d, enlarged.height = %d (area = %d)" % (enlarged.width, enlarged.height, enlarged.area()))


#
## Special Methods
#

# __dict__ returns the properties of an object
print(r.__dict__) # note that no parentheses are used for the method
print(Rectangle.__dict__)

# __eq__ for object equality: without it, == will evaluate reference equality
class A:
  def __init__(self, val):
    self.val = val

print(A('b') == A('b'))


r1 = Rectangle(2, 3)
r2 = Rectangle(2, 3)
print(r1 == r2)

# __repr__ is the proverbial toString
r = Rectangle(3.5, 4.25)
print(r)

#
## operator overloading
#
print(10 * Rectangle(3, 2))
print(Rectangle(2, 5) * 2)

#
## class methods
#
print(Rectangle.square(5))

#
## inheritance
#
class Square(Rectangle):
  def __init__(self, s):
    super().__init__(s, s) # no need to return

  # overridding __scale_, as super().scale() returns a Rectangle
  def scale(self, factor):
    return Square(self.width * factor)

  # overriding __repr__
  def __repr__(self):
    return "Square (%r)" % self.width

sq = Square(5)
print(sq, sq.area())
print(sq.scale(2))

#
## abstract classes: an abstract class must inherit from ABC, a special base class
#
from abc import ABC, abstractmethod

# The Shape abstract class
class Shape(ABC):
  @abstractmethod
  def area(self):
    pass

  @abstractmethod
  def scale(self, factor):
    pass

  def __eq__(self, other):
    return self.__dict__ == other.__dict__

  def __mul__(self, factor):
    return self.scale(factor)

  def __rmul__(self, factor):
    return self.scale(factor)

class Rectangle_v2(Shape):
  def __init__(self, w, h):
    self.width = w
    self.height = h

  def area(self):
    return self.width * self.height

  def scale(self, factor):
    return Rectangle_v2(self.width * factor, self.height * factor)

  def __repr__(self):
    return "Rectangle_v2 (%r by %r)" % (self.width, self.height)

r = Rectangle_v2(3, 4)
print(r, type(r))

print("area(r)=%r" % r.area())
print(Rectangle_v2(5, 3).area())

enlarged = r.scale(2)
print(enlarged)

print(10 * Rectangle_v2(3, 2))
print(Rectangle_v2(2, 5) * 2)

r1 = Rectangle_v2(2, 3)
r2 = Rectangle_v2(2, 3)
print(r1 == r2)

from math import pi
class Circle(Shape):
  def __init__(self, r):
    self.radius = r

  def area(self):
    return pi * (self.radius ** 2)

  def scale(self, factor):
    return Circle(self.radius * factor)

  def __repr__(self):
    return "Circle (radius %r)" % self.radius

circle = Circle(2)
print(circle, type(circle))

print(circle.area())
big_circle = circle.scale(2)
print(big_circle, big_circle.area())