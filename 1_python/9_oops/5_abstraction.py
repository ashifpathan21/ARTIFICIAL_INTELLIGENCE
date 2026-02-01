# to make some rules to follow
# can achieved using library
from abc import ABC , abstractmethod


class abstract (ABC):
    @abstractmethod
    def area(self):
        pass
    def perimeter(self):
        pass

class Square(abstract):
    def __init__(self ,side):
        super().__init__()
        self.side = side

    # must have to create 
    def area(self):
        print(f"Area of square of side {self.side} is {self.side * self.side}")

    def perimeter(self):
        print(f"Perimeter of square of side {self.side} is {4 * self.side}")

sq = Square(4)
sq.area()
sq.perimeter()