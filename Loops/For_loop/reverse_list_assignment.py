'''Laura V. Bullock
10/10/2024
Week6 - Day2
LabCake2-Reversing a List - reverse_list_assignment.py

Objective: Practice reversing a list and transferring its elements into a new list using loops.
Task: Write a Python program that works with the list called laura_things containing the following items:
"sewing machine"
"scissor"
"cutting mat"
"television"
- Your program should do the following:
- Create a list called laura_things with the items listed above.
- Reverse the order of the items in laura_things.
Transfer each item from the reversed list into a new list called reversed_things.
- Print out the new list reversed_things to show that it contains the items in reverse order.

Requirements:
- You must reverse the list using slicing or a loop (do not use Python's built-in reverse methods like reverse() ).
- The final output should look like this:
['television', 'cutting mat', 'scissor', 'sewing machine']

Bonus Challenge:
- After reversing the list and creating reversed_things, print a message that says: "The list has been successfully reversed!"
Submission
- Please submit your code by [insert due date here] in a file named reverse_list_assignment.py. Make sure to test your code to ensure it produces the correct output'''

#Create a list called laura_things
laura_things = ["sewing machine", "scissor", "cutting mat", "television"]
print("\nThe original laura_things list is:\t\t", laura_things)

# FOR LOOP to print each item individually.
for thing in laura_things:
    print("\t", thing)

#Reverse the order of the items in laura_things
reversed_things = laura_things[::-1]

#Bonus Challenge:  The final message after reversing the list
print("\nThe list has been successfully reversed!\t", reversed_things)
for reversed_thing in reversed_things:
    print("\t", reversed_thing)