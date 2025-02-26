class ToUpper:
    def __init__(self):
        self.letter = ''
    
    def GetString(self):
        self.letter = input("Enter: ")
        
    def PrintString(self):
        print(self.letter.upper())
        
a = ToUpper()
a.GetString()
a.PrintString()
