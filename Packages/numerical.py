# Function to check if a given year is a leap year
def isLeapYear(year):
    if year%400==0 or(year%100!=0 and year%4==0):
        return True
    else:
        return False
isLeapYear(2020)




# Function to print n Natural numbers using while loop
def nNaturalNumbers(n):
    counter = 1
    while counter <= n:
        print(counter, end=" ")
        counter = counter + 1
    return
nNaturalNumbers(10)



# Function to check factors of a given number
def factorial(n):
    fact = 1
    for i in range(2, n+1):
        fact = fact * i
    return fact
factorial(4)



# Function to validate the phone number

import re
def phoneNumberValidator(number):
    pattern = '[6-9][0-9]{9}$|[0][6-9][0-9]{9}$|^[+][9][1][6-9][0-9]{9}$'
    if re.match(pattern, str(number)):
          print("valid number")
    else:
          print("invalid number")
phoneNumberValidator(738252496)

