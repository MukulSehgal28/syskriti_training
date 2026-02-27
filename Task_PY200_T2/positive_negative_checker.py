num = int(input("Enter a number: "))

# checking number type
if num > 0:
    print(f"Your entered number {num} is positive")
elif num < 0:
    posValue = num * -1
    print(f"Your entered number {num} was negative , how ever positive value of your number is {posValue}")
else:
    print(f"Your entered number {num} is zero")