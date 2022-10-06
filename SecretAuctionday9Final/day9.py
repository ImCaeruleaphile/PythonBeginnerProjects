#Python Dictionary
codeForUsuages={
    "HTML":"Hyper text Make up Language",
    "Javascript":"function for website",
    "Python":"Versatile!"
}
print(codeForUsuages["Python"])

codeForUsuages["Java"]="For Mobile,Desktop and Web"
print(codeForUsuages)
# empty_dictionary={}
# codeForUsuages=empty_dictionary
# print(codeForUsuages)
for key in codeForUsuages:
    print(key)
    print(codeForUsuages[key])

#Grading Program
students_scores={
    "Chris":44,
    "Hemsworth":55,
    "Cristiano":77,
    "Roanldo":99
}
students_grades={}
for student in students_scores:
    score =students_scores[student]
    if score > 90:
      students_grades[student] = "You are GOAT"
    elif score > 70:
      students_grades[student]="Hey Hey Not Bad,Keep Going"
    elif score >50:
      students_grades[student] = "You need to try more"
    else:
      students_grades[student]="You are obviously failed,But Dont depressed Try Again"
print(students_grades)

#Nesting
#Nesting list in a dictionary
travel_l={
    "France":["Marseille","Paris","Lyon"],
    "Germany":"berlin"
}
#Nesting dictionary in a dictionary
travel_l_={
    "France":{"cityVisited":["Lyon","Paris","Marseille"],"totalReached":7},
    "England":{"cityVisited":["Manchester,Chelsea,Tower Bridge"],"totalReached":9}
}
#Nesting list in a list
travel_l=[
    {"country":"United States","cityVisited":["Los angles,Califonia,Chicago"],"totalReached":77},
    {"country":"Portugal","cityVisited":["Lisbon"],"totalReached":1}
]
#Dictionary In List Exercise
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(Country,Visits,Cites):
    newCountry={}
    newCountry["country"]=Country
    newCountry["visits"]=Visits
    newCountry["cities"]=Cites
    travel_log.append(newCountry)

add_new_country("United States",77,["Chicago","San Fransisco","Paris"])
print(travel_log)

#Blind Auction Program
import day9artModule
print(day9artModule.logo)
bids={}
bidding_finished=False

def find_highest_bid(bid_record):
    highest_bid=0
    winner=""
    for bidder in bid_record:
        bid_amount=bid_record[bidder]
        if bid_amount >highest_bid:
            highest_bid = bid_amount
            winner =bidder
    print(f"The winner is {winner},with the bid of {highest_bid}")
while not bidding_finished:
    name=input("Enter the bidder's name:")
    price=int(input("Enter the bid amount"))
    bids[name]=price
    another_bidder=input("Anyone else wanna bid?y to Yes and n for no")
    if another_bidder=="no":
      bidding_finished=True

find_highest_bid(bid_record=bids)