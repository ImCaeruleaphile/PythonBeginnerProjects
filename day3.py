#Even or Odd
number=int(input("Enter your number to check even or odd: "))
if number % 2==0:
    print("It's even number")
else:
    print("It's odd number")

#Rollacoster
print("Welcome from rollacoster World")
height=int(input("Enter your height"))

bill=0
if height>120:
    print("You Can ride Rolla")
    age=int(input("Enter your age for paying bill"))
    if age<12:
        bill+=5
        print("pay for 5$")
    elif age>18:
        bill+=7
        print("pay for 7$")
    elif (age >22 and age<30):
        bill+=12
        print("pay for 12$")
    elif age>77:
        print("Wow,you are lucky,You can ride rolla free forever")
    else:
        print("pay for 15$")
    wants_photo=input("Want photo for Y and N for No")
    if(wants_photo=="Y"):
        bill+=3
        print("You will get photos")
    else:
        print("Ok")

else:
    print("You can't ride Rolla,Go and drink appeton")
print("You total bill for rolla costa is ->"+str(bill))

#leap year
year=int(input("Enter the year to check leap year or not: "))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")
print(f"The year you check is {year}")

#Pizza Order
size=input("Enter your pizza size 'L','M','S'")
pepper=input("Do you wanna put pepper to pizza?Yes or No")
cheese=input("More cheese want or not?Y or N")

bill=0
if size=='L':
    bill+=9
elif size=='M':
    bill+=7
else:
    bill+=3
if pepper=="Yes":
    bill +=3
else:
    bill +=0
if cheese=="Y":
    bill+=2

print(f"Your final bill is {bill}")

#Love Calculator
print("Welcome from fun love calculator")
name1=input("Enter your name:")
name2=input("Enter your other name:")

combined_string= name1+name2

lowercaseString=combined_string.lower()

t=lowercaseString.count("t")
r=lowercaseString.count("r")
u=lowercaseString.count("u")
e=lowercaseString.count("e")

true= t + r + u + e

l=lowercaseString.count("l")
o=lowercaseString.count("o")
v=lowercaseString.count("v")
e=lowercaseString.count("e")

love= l + o + v + e

love_score = str(true) + str(love)

if(love_score<str(10) or love_score>str(90)):
    print(love_score)
    print("You two are together like elon musk and working hard")
elif(love_score<str(40) and love_score>str(50)):
    print("It's possible to do wedding with your lover")
else:
    print(f"Your love score is {love_score}")

#Treasure Island
print("Welcome from the treaure Island Game for Life")

chance=input("If life give two choices-1'Do nothing and Lazy' and 2'To become a professional programmer',What would you choice?")
if chance=="2":
    tool=input("You got lot of money from IT Job.You want to choice 1'Buy PC and Work smart than before' 2'Wasting all with chill'")
    if tool=="1":
        que=input("Answer me 1'Programming is hard and not fun' 2'Programming is fun so much'")
        if que=="2":
            print("YoHo,Congratulations,Greatest Programmer of All Time.")
        else:
            print("Oh my gosh,I think you are a real programmer but you are not.")
    else:
        print("You are not a real programmer.It's Game Over Now")
else:
    print("You are game over there is nothing interesting in your life")




