
def unique_list(numbers):
    unique = []
    for number in numbers:
        if number not in unique:
            unique.append(number)
    return unique


user_input = input("enter a numbers: ")


numbers = list(map(int, user_input.split()))


print("unigue numbers: ", unique_list(numbers))
