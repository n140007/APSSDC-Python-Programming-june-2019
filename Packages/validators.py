# Function to validate the phone number

import re
def phoneNumberValidator(number):
    pattern = '[6-9][0-9]{9}$|[0][6-9][0-9]{9}$|^[+][9][1][6-9][0-9]{9}$'
    if re.match(pattern, str(number)):
          print("valid number")
    else:
          print("invalid number")
phoneNumberValidator(7382524966)

def emailValidator(email):
    pattern = '^[0-9a-z][0-9a-z_.]{4,13}[0-9az][@][0-9a-z]{3,18}[0-9a-z][.][a-z]{2,4}$'
    if re.match(pattern,email):
        return True
    else:
        return False
emailValidator("mangadevigalla@gmail.com")