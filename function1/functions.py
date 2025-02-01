import math
from random import randint
def volume_ball(r):
    return (4/3) * math.pi * (r ** 3)

def polindrom(st):
    cleaned_st = ""
    for char in st:
        if char != " ":
            cleaned_st += char.lower()
    a=0
    b=len(st)-1
    while a<b:
        if st[a]!=st[b]:
            return False
        a+=1
        b-=1
    return True

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

def histogram(lst):
    for i in lst:
        print("*"*i)