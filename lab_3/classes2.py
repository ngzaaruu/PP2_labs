class Shape:
    def __init__(self, a=0):
        self.a = a
    
    def area(self):
        return 0  

class Square(Shape):
    def __init__(self, length):
        super().__init__(length)  
    
    def area(self):
        return self.a ** 2  

shape = Shape()
print("area of shape:", shape.area()) 

square = Square(4)  
print("area of square:", square.area()) 
