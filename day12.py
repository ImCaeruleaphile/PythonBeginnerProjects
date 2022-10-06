#Scope

favLangs=3
def total_fav():
    favLangs=7
    print(f"You have total {favLangs} favourite languages")
total_fav()
print(f"You have total {favLangs} favorite languages")

#Modifying global Scope
enemies=1
def total_enemies():
    #global enemies
    print(f"You have {enemies} enemies")
    return enemies - 1

enemies =total_enemies()
print(f"You have {enemies} enemies")

#Number Guessing Game

#Random choose number between 1 and 100
import random
EASY_ATTEMPTS=10
HARD_ATTEMPTS=5
#Check guess is Right or Wrong
def check_guess(guess,answer,turns):
    if guess >answer:
        print("Too high")
        return turns-1
    elif guess < answer:
        print("Too low")
        return turns-1
    else:
        print(f"You guessed the answer = {answer},You wins")
#Check user's chosen difficuity
def set_difficulty():
    level=input("type 'easy' to easy level game,and 'hard' to hard game")
    if level=="easy":
        return EASY_ATTEMPTS
    elif level =="hard":
        return  HARD_ATTEMPTS
#print(f"The answer: {answer}")
def game():
    print("Welcome from the number guessing game")
    print("I am thinking number between 1 and 100")
    answer=random.randint(1,100)
    turns= set_difficulty()
    print(f"You have {turns} attempts remaining to guess the number")

    #repeat the guess function if it's wrong
    guess=0

    while guess != answer:
        #let user guess the number
        guess=int(input("Enter the guess: "))
        #track the number reduce 1 if it's wrong
        turns =check_guess(guess,answer,turns)
        if turns==0:
            print("You are run out of turns,You lost the guess Game")
            return
        elif guess != answer:
            print("Guess Again")

game()