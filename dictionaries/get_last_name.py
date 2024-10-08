'''Laura V. Bullock
10/4/2024
Week5 - Day2
Homework-get_last_name.py

- Print out the last name of the second employee.  Please search through the dictionary below: **Alexandra ☺️
'''

h2_dictionary = {"employees": [{"firstName": "John", "lastName": "Doe"},\
                    {"firstName": "Anna", "lastName": "Smith"},
                    {"firstName": "Peter", "lastName": "Jones"}],
                "owners": [{"firstName": "Jack", "lastName": "Petter"},
                    {"firstName": "Jessy", "lastName": "Petter"}]}

search = "Alexandra"

# #printing the full employees dictionary
# print(f'\nThe "employees" dictionary consists of:\n', h2_dictionary["employees"])

# #printing index 1, which is where the 2nd employee resides
# print(f'\nIndex 1 of the "employees" dictionary is:\t', h2_dictionary["employees"][1])

#printing the Second employee's last name
print(f'\nThe last name of the second employee is:\t', h2_dictionary["employees"][1]["lastName"])


if search not in h2_dictionary["employees"][0]["firstName"] and \
    search not in h2_dictionary["employees"][1]["firstName"] and \
    search not in h2_dictionary["employees"][2]["firstName"] and \
    search not in h2_dictionary["owners"][0]["firstName"] and \
    search not in h2_dictionary["owners"][1]["firstName"] and \
    search not in h2_dictionary["employees"][0]["lastName"] and \
    search not in h2_dictionary["employees"][1]["lastName"] and \
    search not in h2_dictionary["employees"][2]["lastName"] and \
    search not in h2_dictionary["owners"][0]["lastName"] and \
    search not in h2_dictionary["owners"][1]["lastName"]:
    print(f'\nEntry Not Found for "{search}"!')
else:
    print(f'\n{search}')