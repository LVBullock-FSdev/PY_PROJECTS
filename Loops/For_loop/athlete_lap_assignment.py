'''Laura V. Bullock
10/10/2024
Week6 - Day2
LabCake1-Looping through Athletes - athlete_lap_assignment.py

Objective: Practice using loops to iterate through a list and display information.
Task: Write a Python program that uses a list of four U.S. women athletes who have competed in the 400 meters at the Olympics. Your program should do the following:
1.  Create a list called athletes with the following names:
- Allyson Felix
- Sanya Richards-Ross
- Shaunae Miller-Uibo
- Phyllis Francis
2.  Use a for loop to display each athlete's name along with the lap number they completed. The output should be in the following format:
- Lap 1: Allyson Felix has completed their lap!
- Lap 2: Sanya Richards-Ross has completed their lap!
- Lap 3: Shaunae Miller-Uibo has completed their lap!
- Lap 4: Phyllis Francis has completed their lap!

Requirements:
- Do not use the enumerate() function.
- Use a counter variable to keep track of the lap number.

Bonus Challenge:
- Modify your code to display a message at the end that says: "All athletes have completed their laps!"
Submission
- Please submit your code  in a file named athlete_lap_assignment.py and upload it to gihub. Make sure to test your code to ensure it produces the correct output.'''

#Create a list called athletes
athletes = ["Allyson Felix", "Sanya Richards-Ross", "Shaunae Miller-Uibo", "Phyllis Francis"]

print("\n")

#Use a for loop to display each athlete's name along with the lap number they completed
for index in range(len(athletes)):
    print(f"Lap {index + 1}: {athletes[index]} has completed their lap!" )

# Bonus - Final message after all athletes have completed their laps
print("\nAll athletes have completed their laps!")

