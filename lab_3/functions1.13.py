import random

def GuessTheNumber():
    
    print("Hello! What is your name?")
    
    name = input()
    
    number = random.randint(1, 20)
    
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    a = 0 #попытки
    
    while True:
        print("Take a guess.")
        guess = int(input())
        a += 1
        
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
           
            print(f"Good job, {name}! You guessed my number in {a} guesses!")
            break

GuessTheNumber()