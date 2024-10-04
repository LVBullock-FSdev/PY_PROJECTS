'''Laura V. Bullock
10/4/2024
Week5 - Day2
Homework-get_last_name.py

- Print out the last name of the second employee.  Please search through the dictionary below:
'''

h2_dictionary = {"employees": [{"firstName": "John", "lastName": "Doe"},\
                               {"firstName": "Anna", "lastName": "Smith"},
                               {"firstName": "Peter", "lastName": "Jones"}],
                "owners": [{"firstName": "Jack", "lastName": "Petter"},
                           {"firstName": "Jessy", "lastName": "Petter"}]}

# #printing the full employees dictionary
# print(f'\nThe "employees" dictionary consists of:\n', h2_dictionary["employees"])

# #printing index 1, which is where the 2nd employee resides
# print(f'\nIndex 1 of the "employees" dictionary is:\t', h2_dictionary["employees"][1])

#printing the Second employee's last name
print(f'\nThe last name of the second employee is:\t', h2_dictionary["employees"][1]["lastName"])