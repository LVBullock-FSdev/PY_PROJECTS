'''
Laura V. Bullock
10/16/2024
Week7
Interview Challenge-fruit_upper_sort.py

Write a python program that creates a list with the following:

3, BaNanA 
2, ApplE
4,Orange
2,ApplE
10,Grape
1,CherrY
3, banana
10,Grape

Then display the output below: 

1,CHERRY
2,APPLE
2,APPLE
3,BANANA
3,BANANA
4,ORANGE
10,GRAPPE
10,GRAPPE'''

# Create the list
fruits = [
    (3, "BaNanA"),
    (2, "ApplE"),
    (4, "Orange"),
    (2, "ApplE"),
    (10, "Grape"),
    (1, "CherrY"),
    (3, "banana"),
    (10, "Grape")
]

print(f"\nThe original list:  ", fruits)

# Process the list: convert fruit names to uppercase
processed_fruits = [(num, fruit.upper()) for num, fruit in fruits]

# # Sort the list by the numeric value
processed_fruits.sort()

print(f"\nThe list after changing to uppercase and sorting: \n")
# Display the output
for num, fruit in processed_fruits:
    print(f"{num},{fruit}")