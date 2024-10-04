'''Laura V. Bullock
10/4/2024
Week5 - Day2
Homework-english_french_translator.py

- Create an English to French translator program.
- The programs takes a word from the user as an input and translates it using a dictionary data type as a vocabularey word.
- Please add the translation of "prun" in your homework.
- If the word is not in the code french, print "[word]" is not in memory)
***The user will select the language the would like to translate to*** (optional)
'''

#get user input
user_input = input('\nSelect from the list below or enter a word.\
                   \n\tcloud\n\tspace\n\tassigns\n\tchallenging homework\n\tno prune here\
                   \nPlease enter a word here-->   ')

#declaration for word not in memory
not_in_memory = f'\nSorry, the word "{user_input.upper()}" is not in memory today, but we can add it in the future.'

# declare an empty dictionary
french = {}

#Add to the dictionary
french["cloud"]= "nuage"
french["space"] = "espace"
french["assigns"] = "assigne"
french["challenging homework"] = "devoirs difficiles"
french["no prune here"] = "pas de pruneau ici"

translation = f'\nThe French translation of "{user_input.upper()}" is:\t'

if user_input == "cloud":
    print(translation, french.get('cloud'))
elif user_input == "space":
    print(translation, french.get('space'))
elif user_input == "assigns":
    print(translation, french.get('assigns'))
elif user_input == "challenging homework":
    print(translation, french.get('challenging homework'))
elif user_input == "no prune here":
    print(translation, french.get('no prune here'))
else:
    print(not_in_memory)