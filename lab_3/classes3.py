class Shape:
    def area (self):
        return 0

class Rectangle(Shape):
    
    def __init__(self):
        self.a = int(input("Enter l:"))
        self.h = int(input("Enter w:"))
        
    def area(self):
        print((self.a * self.h)/2)

r = Rectangle()
r.area()
    