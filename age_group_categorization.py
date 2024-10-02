'''Laura V. Bullock
9/26/2024
Week4 - Day2
LabCake3-age_group_categorization.py

Prompt the user to enter their age as an integer and display the appropriate life stage.
If the user enters a negative number or a non-realistic number (e.g. more than 150), display and "Invalid age" message.'''

age = int(input("Please enter your age:\t"))
age_msg = f"The age entered is:  {age}. This person is a(n):\t"
invalid_msg = f"The age entered is:  {age}.  Invalid age! You have failed the human test.  Please try again."

#Based on the input, categorize the person into one of the following life stages:

#Invalid entry
# if age < 0 or age > 150:
#   print(invalid_msg)
#Infant: 0-1 year
if age == 0 or age == 1:
  print(age_msg + "INFANT")
#Toddler: 2-3 years
elif age == 2 or age == 3:
  print(age_msg + "TODDLER")
#Child: 4-12 years
elif age >= 4 and age <= 12:

# elif age == 4 or age < 13:
  print(age_msg + "CHILD")
#Teenager: 13-19 years
elif age >= 13 and age <= 19:
  print(age_msg + "TEENAGER")
#Adult: 20-64 years
elif age >= 20 and age <= 64:
  print(age_msg + "ADULT")
#Senior: 65 years and older
elif age >= 65 and age <= 150:
  print(age_msg + "SENIOR")
else:
  print(invalid_msg)