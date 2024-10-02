'''Laura V. Bullock
10/2/2024
Week5 - Day1
Homework-get_min_max.py

- Write a Python program that prints the largest and smallest values in a list.
- Print the two values on the same line, separated by a space.
- The largest value should appear first and the smallest value should appear second.
- You may assume that the list only contains numeric values
- If the list is empty, print "None."

Expected output:
[3,4,5,6]       --> 6 3
[-1,-2,-3,-4]   --> -1 -4
[0,0,0,0]       --> 0 0
[]              --> []
'''

#my_list = [3,4,5,6]
#my_list = [-1,-2,-3,-4]
#my_list = [0,0,0,0]
my_list = [] 

if len(my_list) != 0:
    print(max(my_list), min(my_list))
else:
    print(my_list, "None")