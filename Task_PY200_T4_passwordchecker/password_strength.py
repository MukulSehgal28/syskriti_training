password = input("Enter password: ")

hasDigit = False
hasUpper = False
hasLower = False
lengthOk = False

#checking password length
if len(password) >= 8:
    lengthOk = True

for ch in password:
    #checking digit
    if ch >= '0' and ch <= '9':
        hasDigit = True
    #checking uppercase
    if ch >= 'A' and ch <= 'Z':
        hasUpper = True
    #checking lowercase
    if ch >= 'a' and ch <= 'z':
        hasLower = True

if lengthOk and hasDigit and hasUpper and hasLower:

    print("Your Password is STRONG")
else:
    print("Your Password is WEAK \n Please make sure your password has at least 8 characters, \n contains at least one digit, \n one uppercase letter and one lowercase letter")