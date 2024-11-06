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
    # Open the the file in write mode
    with open(elements_file, 'w') as file:
        #Loop through each element in the list and write to the file.
        for element in elements:
            file.write(f"{element}\n")

    #Stripping the last empty line from the file
    # Read the list from the file
    with open(elements_file, 'r') as f:
        lines = f.readlines()

    # Strip the newline from the last element
    if lines:
        lines[-1] = lines[-1].rstrip('\n')

    # Write the modified list back to the file
    with open(elements_file, 'w') as f:
      f.writelines(lines)

elements = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Flourine", "Neon"]

print(elements)

list_to_file(elements_file, elements)