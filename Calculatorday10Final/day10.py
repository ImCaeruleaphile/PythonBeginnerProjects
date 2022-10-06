#Functions with Outputs
#Return

def formatted_name(f_name,l_name):
    formatted_f=f_name.title()
    formatted_l=l_name.title()
    return f"{formatted_f} {formatted_l}"
print(formatted_name("hTet","crIsTiAno"))

#MultipleReturns
def formatted_fl(f_n,l_n):
    if f_n=="" and l_n=="":
        return "Please type first Name and Last Name of Your Idol"
    formatted_fname=f_n.title()
    formatted_lname=l_n.title()
    return f"Your Idol name is {formatted_fname} {formatted_lname}"
print(formatted_fl(input("Enter the first Name"),input("Enter the last Name")))

#Days in Month
def is_leap(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        print("Not leap year")
def days_in_month(year,month):
    if month>12 and month<0:
        print("Invaid Month")
    month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap(year) and month==2:
        return 29
    return month_days[month-1]

year=int(input("Enter the year"))
month=int(input("Enter the month"))
days=days_in_month(year,month)
print(days)

#Calculator

def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    import art
    print(art.logo)
    num1=int(input("Enter the first number: "))
    for symbol in operations:
        print(symbol)
        should_continue=True

    while should_continue:
        operation_symbol=input("Choose the operation from the line above: ")
        num2=int(input("Enter the second number: "))
        calculation_function= operations[operation_symbol]
        answer= calculation_function(num1,num2)

        print(f"{num1} {operation_symbol} {num2}= {answer}")

        if input(f"Enter 'y' to continue calculating with {answer},and n to start a new calculation")=="y":
            num1=answer
        else:
            should_continue=False
            '''Recursive'''
            calculator()
calculator()



