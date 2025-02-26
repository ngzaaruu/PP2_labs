def prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def filter_prime(nums):
    return [num for num in nums if prime(num)] 

nums = list(map(int, input("Enter: ").split()))
primes = filter_prime(nums)
print("Prime numbers:", primes)
