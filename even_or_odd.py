'''Laura V. Bullock
9/26/2024
Week4 - Day2
LabCake1-Check for even or odd

Write a program that will ask a user for a number then check whether that number is EVEN or ODD.

Display on the screen:
Please enter a number between 1-100
Your number user_number is even/odd.
'''

user_number = float(input("Please enter a number between 1-100:\t"))

if user_number % 2 == 0:
    print(f"Your number {user_number} is EVEN")
else:
    print(f"Your number:  {user_number} is ODD.")