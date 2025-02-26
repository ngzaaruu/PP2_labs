def histogram(nums):
    
    for num in nums:
        print("*" * num)
        
input = input("Enter: ")
hist = list(map(int, input.split()))

histogram(hist)