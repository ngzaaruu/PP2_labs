class Shape:
    
    def area(self):
        return 0
    
class Square(Shape):
    
    def __init__(self):
        self.lenght = int(input("Enter:"))
        
    def area (self):
        print(self.lenght**2)

a = Square()
a.area()