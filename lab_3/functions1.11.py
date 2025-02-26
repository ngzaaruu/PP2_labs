def palindrome(p):
    
    p = p.lower()
    
    return p == p[::-1]

a = input("Enter: ")
if palindrome(a):
    print("This is palindrome")
    
else:
    
    print("This is not palindrome")