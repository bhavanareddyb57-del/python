#elif statement
#question 1 
a = 10 
b = 20
if a>=15:
    print("a is greater than b")
elif a>=20:
    print("a is equal to b")
else:
    print("a is less than b")

#question 2
#we can use elif statement as many times as we want
#using 'and' operator
marks = int(input("enter marks: "))
if marks>=90:
    print("grade A")
elif marks<=89 and marks>=60:
    print("grade B")
elif marks<=59 and marks<=35:
    print("grade C") 
else:
    print("grade D")

#question 3 
marks = int(input("enter marks"))
if marks>=90:
    print("grade A")
elif marks >=75:
    print("grade B")
elif marks>=60:
   print("grade C")
elif marks>=40:
    print("grade D")
else:
    print("fail")

#question 4 
#greatest of three numbers
a = int(input("enter 1st number: "))
b = int(input("enter 2nd number: "))
c = int(input("enter 3rd number: "))
if a>b and a>c:
    print("a is the greatest")
elif b>a and b>c:
    print("b is the greatest")
else:
    print("c is the greatest")

#question 5
#largest of two numbers 
a = int(input("enter 1st number: "))
b = int(input("enter 2nd number: "))
if a>b:
    print("a is largest")
elif b>a:
    print("b is largest")
else:
    print("both are equal")

#question 6

#question 7
day = int(input("enter day number: "))
if day == 1:
    print("monday")
elif day == 2:
    print("tuesday")
elif day == 3:
    print("wednesday")
elif day == 4:
    print("thursday")
elif day == 5:
    print("friday")
elif day == 6:
    print("saturday")
elif day==7:
    print("sunday")
else:
    print("invalid day")


#if statement
# question 1
a = 10 
b = 20 
if (a<b):
    print("a is less than b")

#question 2 
A = 10 
B = 5 
if (A>B):
    print("A is greater than B")

#question 3 
age = 18 
if (age>=18):
    print("Eligible for voting")

#question 4
marks = 90
if marks>=40:
    print("pass")

#question 5
number = int(input("enter number"))
if number%5 == 0:
    print("divisible ny 5")

#question 6 
#temperature check 
temperature = float(input("enter temperature"))
if temperature > 40:
    print("high temperature")


#if else statement
#question 1
a = 10
b = 20 
if (a>b):
    print("a is greater than b")
else:
    print("a is less than b")

#question 2 
A = 20 
B = 10 
if (A>B):
    print("A is greater than B")
else:
    print("A is less than B")

#question 3 
age = int(input("enter age: "))
if (age>=18):
    print("Eligibile for voting")
else:
    print("Not Eligible for voting")

#without brackets, the code will be executed 
    age = 20
    if age>=18:
        print("eligible")
    else:
        print("not eligible")

#question 4
marks = 35
if marks>=40:
    print("pass")
else:
    print("fail")

#question 5 
number = int(input("enter number"))
if number % 2 == 0:
    print("even")
else:
    print("odd")

#question 6 
#temperature check 
temperature = float(input("enter temperature"))
if temperature > 40:
    print("high temperature")
else:
    print("low temperature")

#question 7 
num = int(input("enter a number: "))
if num>=0:
    print("positive")
else:
    print("negative")

#question 8
    num = int(input("enter a number: "))
    if num>100:
        print("number is greater than 100")
    else:
        print("number is not greater than 100")


#nested if        
#question 1 
username = input("enter username: ")
password = int(input("enter password: "))
if (username == "admin123"):
    if (password == 1234):
        print("login successful")
        
    else:
        print("wrong password")
else:
    print("wrong username")

#question 2 
a = float(input("enter first number:"))
b = float(input("enter second number: "))
operator = input("enter operator (+, -, *, /): ")
if operator == "+":
    print("result:", a+b)
elif operator == "-":
    print("result:", a-b)
elif operator == "*":
    print("result:", a*b)
elif operator == "/":
    if b!=0:
        print("result:",a/b)
    else:
        print("error: division by zero is not allowed")
else:
    print("invalid operator")

#question 3
marks = int(input("enter marks: "))
attendance = int(input("enter attendance percentage: "))
if marks >= 40:
    if attendance >= 75:
        print("pass")
    else:
        print("fail due to low attendance")
else:
    print("fail due to low marks")

#question 4
balance = float(input("enter account balance: "))
amount = float(input("enter withdrawal amount: "))
if amount > 0:
    if amount <= balance:
        balance =  balance - amount
        print("withdrawal successful")
        print("remaining balance:", balance)
    else:
        print("insufficient balance")
else:
    print("invalid withdrawal amount")

#question 5
age = int(input("enter age: "))
test = input("did you pass the driving test? (yes/no): ")
if age >= 18:
    if test == "yes":
        print("eligible for driving license")
    else:
        print("pass the driving test first")
else:
    print("not eligible due to age")

   









































