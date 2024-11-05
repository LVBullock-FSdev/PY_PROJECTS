'''Laura V. Bullock
11/4/2024
In-Class Challenge-Elements of a list to a file.

Write a Python program that writes the elements of a list to the file denoted by the variable file.
Each element should be written on a separate line.
The file should be new or its existing content must be replaced by this new content.
  Expected Output:
If this is the list:
[1, 2, 3, 4, 5]
After running the program, the content of the file should be:
1
2
3
4
5
  Hints:
•	You will need to add a \n (new line) character to write the elements on separate lines.
'''

'''
Modes
w = write
r = read
a = append'''

elements_file = 'elements_to_list.txt'
#The most efficient way is to create a function with a loop to get line by line
def list_to_file(elements_file, elements):
    with open(elements_file, 'w') as file:
        for element in elements:
            file.write(element)

elements = ["Hydrogen\n", "Helium\n", "Lithium\n", "Beryllium\n", "Boron\n", "Carbon\n", "Nitrogen\n", "Oxygen\n", "Flourine\n", "Neon"]

print(elements)

list_to_file(elements_file, elements)