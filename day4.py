import random

randomInterger=random.randint(1,10)
print(randomInterger)

randomFloat=random.random()*5
print(randomFloat)

love_score=random.randint(1,100)
print(f"You and your lover love score is {love_score}")

#Bank roulette
names_string=input("Enter the names for paying the bill:")
names=names_string.split(", ")

# name_items=len(names)
# random_choice=random.randint(0,name_items-1)
# person_who_pay=names[random_choice]
# print(names)
person_who_pay=random.choice(names)
print(f"{person_who_pay} will pay for this meal")

#Treasure Map
rows1=["","",""]
rows2=["","",""]
rows3=["","",""]

map=[rows1,rows2,rows3]

position=input("Where do you want to your treasure : ")

horizontal=int(position[0])
vertical=int(position[1])

selected_row=map[horizontal-1]
selected_row[vertical-1]="Y"
# map[vertical-1][horizontal-1]="X"

print(f"{rows1}\n{rows2}\n{rows3}")

#Rock,Paper,Scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
game_images=[rock,paper,scissors]
print("Welcome from Rock,Paper,Scissors Game")
user_choice=int(input("Zero For Rock,1 For Paper and 2 For Scissors"))

if(user_choice>=3 or user_choice<0):
    print("Please type a vaild number")
else:
    print(game_images[user_choice])

computer_choice=random.randint(0,2)
print(game_images[computer_choice])

if(user_choice==0 and computer_choice==2):
    print("You wins")
elif (user_choice==2 and computer_choice==0):
    print("Computer wins")
elif(user_choice>computer_choice):
    print("You wins")
elif(user_choice<computer_choice):
    print("Computer wins")
elif(user_choice==computer_choice):
    print("It's draw")




