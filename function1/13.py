from random import randint

def guess_the_num():
    a = 1
    name = input("Hello! What is your name? ")
    guess_num = randint(1, 20)
    
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    num = int(input("Take a guess: "))
    
    while num != guess_num:
        if num < guess_num:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
        
        num = int(input("Take a guess: "))
        a += 1
    
    print(f"Good job, {name}! You guessed my number in {a} guesses!")


guess_the_num()
