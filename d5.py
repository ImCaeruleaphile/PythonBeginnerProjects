#Loops
langs=["Java","Python","CSharp"]
for lang in langs:
    print(lang)
#Average Height
Students_heights=input("Enter the students heights: ").split()

for n in range(0,len(Students_heights)):
    Students_heights[n] =int(Students_heights[n])

print(Students_heights)

total_height=0
for height in Students_heights:
    total_height += height
total_student=0
for student in Students_heights:
    total_student += 1
average_height=round(total_height/total_student)
print(average_height)
#High Score
students_scores=input("Enter the students scores:").split()

for n in range(0,len(students_scores)):
    students_scores[n]=int(students_scores[n])
print(students_scores)

highest_score=0
for score in students_scores:
    if score > highest_score:
        highest_score += score

print(f"The highest score in the class is {highest_score}")

#For Ranges(Adding even numbers)
total1=0
for number in range(2,101,2):
    total1 += number
print(total1)

total2=0
for number in range(1,101):
    if number % 2==0:
        total2 += number
print(total2)

#Password Generator
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password=""
for char in range(1,nr_letters+1):
    password += random.choice(letters)
for char in range(1,nr_symbols+1):
    password += random.choice(symbols)
for char in range(1,nr_numbers+1):
    password += random.choice(numbers)
print(password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

passwordList=[]
for char in range(1,nr_letters+1):
    passwordList.append(random.choice(letters))
for char in range(1,nr_symbols+1):
    passwordList.append(random.choice(symbols))
for char in range(1,nr_numbers+1):
    passwordList.append(random.choice(numbers))
print(passwordList)
random.shuffle(passwordList)
print(passwordList)

password=""
for char in passwordList:
    password += char
print(f"The hard Level passwd is {password}")