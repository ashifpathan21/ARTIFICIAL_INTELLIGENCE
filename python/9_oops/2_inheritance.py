class Shape:
    def __init__(self):
        print("Shape is created")


class Rectangle(Shape):
    def __init__(self , length , breadth):
        super().__init__()
        self.length=length
        self.breadth=breadth
    
    def area(self):
        print(f"Area of Rectangle of length {self.length} and breadth {self.breadth} is {self.length * self.breadth}")


rect1 = Rectangle(10 , 20)
rect1.area()

# class default_class(Shape , Rectangle) Multiple inheritance
# Method resolution order --> constructor follows the first inherited class if passed 
