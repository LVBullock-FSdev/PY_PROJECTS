'''CLOUDSPACE ACADEMY
Python-AWS/August 2024
Instructor:  Cloudio Sidi

Laura V. Bullock
9/20/2024
Week3 Day2 
Lab2-body_weight_convertor.py

Write a program that will ask for a user to enter his/her body weight in pounds (lbs) and convert it to kilogram (kg).
Display on the screen: your body weight is weight in lbs, and the equivalent kgs is weight kg.  Thank you!  only display three digit decimal e.g:10.234'''

weight_in_lbs = float(input("Please enter your body weight in pounds (lbs):\t"))
weight_kg  = (weight_in_lbs * 0.453592)

print(f"Your body weight is {weight_in_lbs} in lbs, and the equivalent kgs is {weight_kg:0,.3f}.  Thank you!")