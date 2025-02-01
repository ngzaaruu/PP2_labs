class Shape:
    def __init__(self, a=0):
        self.a = a
    
    def area(self):
        return 0  

class Rectangle(Shape):
    def __init__(self, length, width):
        
        self.length = length
        self.width = width
    
    def area(self):
        
        return self.length * self.width


shape = Shape()

print("area of Shape:", shape.area())  

rectangle = Rectangle(5, 3)  

print("area of rectangle:", rectangle.area())