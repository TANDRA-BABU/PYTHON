## "Number Guessing Games (example of nested condition)"

import random
winning_number= random.randint(1,100)
guess=1
number= int(input("Guess a Number between 1 & 100: "))
game_over=False
while not game_over:
    if number==winning_number:
        print(f"You Win! You guessed this number in {guess} times")
        game_over=True
    else:
        if number<winning_number:
            print("Too Low")
        else:
            print("Too High")
        guess+=1
        number=int(input("Guess Again "))
