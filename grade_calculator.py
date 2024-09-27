'''Laura V. Bullock
9/26/2024
Week4 - Day2
LabCake2-grade_calculator.py

Write a program that will ask a student for their grades in 5 subjects.

Calculate your average grade and print grade from A-E.
A>90
B>80
C>70
D>60
E===Failed

Display on the screen:  Provide the screenshot and github link.  Submit your homework in your github account as well.  Create a folder in Python-codes
'''

grade1 = float(input("Please enter your grade score for English:\t"))
grade2 = float(input("Please enter your grade score for Calculus:\t"))
grade3 = float(input("Please enter your grade score for History:\t"))
grade4 = float(input("Please enter your grade score for Biology:\t"))
grade5 = float(input("Please enter your grade score for Art:\t\t"))

final_score = grade1 + grade2 + grade3 + grade4 + grade5
gpa = final_score / 5
print(f"Your final score for all courses is:\t{final_score}.")

if gpa >= 90:
    print(f"Your GPA is {gpa} -- Grade is A.")
elif gpa >= 80 and gpa < 90:
    print(f"Your GPA is {gpa} -- Grade is B.")
elif gpa >= 70 and gpa < 80:
    print(f"Your GPA is {gpa} -- Grade is C.")
elif gpa >= 60 and gpa < 70:
    print(f"Your GPA is {gpa} -- Grade is D.")
else:
    if gpa < 60:
        print(f"Your GPA is {gpa} -- Grade is E- You have failed.")