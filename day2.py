print("Hello"[0])
changeTyped=str(7777777)
print(type(changeTyped))

#bmi calculator
weight=float(input("Enter your weight :"))
height=float(input("Enter your height :"))

bmi = weight / height**height
print("The result of bmi calculator is :"+str(bmi))

#Life in weeks
age=input("Enter your age for know your Remaining life: ")

age_in_int = int(age)
age_in_years=90-age_in_int
age_in_days= age_in_years * 365
age_in_months= age_in_years * 12
age_in_weeks= age_in_years * 52

print(f"You've remaining {age_in_days} days,{age_in_weeks} weeks and {age_in_months} months before gonna die")
#
# twodigitnumbers=input("Enter your two digit to know your result :")
#
# first_digit= int(twodigitnumbers[0])
# second_digit= int(twodigitnumbers[1])
# Result= first_digit + second_digit
# print(f"Your result is {Result}")

#Tip calculator
print("Welcome from the tip calculator")
bill=float(input("Enter your bill amount: "))
tip=int(input("Enter your tip percent: "))
person=int(input("How many people are pay for this bill: "))

tip_percent= tip / 100
total_tip_amount =tip_percent * bill
total_bill = total_tip_amount + bill
billPerperson= total_bill / person
final_amount="{:.2f}".format(billPerperson)
print(f"Each person should pay {final_amount}")

