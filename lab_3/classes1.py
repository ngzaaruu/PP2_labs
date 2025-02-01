class toUpper:
    def __init__(self):
        self.text = ""
    
    def getString(self):
        self.text = input("Enter: ")
    

    def printString(self):
        print(self.text.upper())

string_manipulator = toUpper()
string_manipulator.getString()  
string_manipulator.printString()  