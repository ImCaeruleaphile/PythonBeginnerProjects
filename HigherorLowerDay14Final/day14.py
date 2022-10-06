#Display art
import art
import game_data
import random

print(art.logo)

#format the random acoount to printable
def format_account(account):
    account_name=account["name"]
    account_descr=account["description"]
    account_coun=account["country"]
    return f"{account_name},a {account_descr} from {account_coun}"

def check_answer(guess,a_followers,b_followers):
    if a_followers > b_followers:
        return  guess =="a"
    else:
        return  guess =="b"
score=0
game_should_continue=True
account_b=random.choice(game_data.data)
#Make the game repeatable
while game_should_continue:
    # Making acoount at position B become in next account at position A

    #Generate the random account from game data
    account_a=account_b
    account_b=random.choice(game_data.data)
    if account_a==account_b:
        account_b=random.choice(game_data.data)

    print(f"Compare A:{format_account(account_a)}")
    print(art.vs)
    print(f"Compare B:{format_account(account_b)}")

    #Ask user for guess
    guess=input("Who has more followers?Type A or B for guessing: ").lower()


    #Check if user is correct

    ##Get follower count of each account
    a_follower_count=account_a["follower_count"]
    b_follower_count=account_b["follower_count"]

    # clear()
    # print(art.logo)
    is_correct=check_answer(guess,a_follower_count,b_follower_count)
    #Give user feedback on their guess
    #Score keeping
    if is_correct:
        score +=1
        print(f"You are right,current Score: {score}")
    else:
        print(f"Your final score is score: {score}")
        game_should_continue=False





