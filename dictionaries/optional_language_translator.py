'''Laura V. Bullock
10/4/2024
Week5 - Day2
Homework-optional_language_translator.py

- Create an English to French translator program.
- The programs takes a word from the user as an input and translates it using a dictionary data type as a vocabulary word.
- Please add the translation of "prune" in your homework.
- If the word is not in the French code, print "[word]" is not in memory)
***The user will select the language that he/she would like to translate to*** (optional)
'''


'''------------------------***OPTIONAL***--------------------------------
***The user will select the language the would like to translate to*** (optional)'''
#get user input
word = input('\nSelect from the list below or enter a word.\
                   \n\tcloud\n\tspace\n\tassigns\n\tchallenging homework\n\tno prunes here\n\tprune\
                   \nPlease enter a word here-->   ')
user_language = input('\nSelect from the list below or enter a language.\
                   \n\tFrench\n\tSpanish\n\t\
                   \nPlease enter a your language preference here-->   ')

#declaration for word not in memory
not_in_memory = f'\nSorry, the word "{word.upper()}" is not in memory today, but we can add it in the future if it is a real word.'

# declare an empty dictionary
languages = {"French": [{"cloud": "nuage"}, {"space": "espace"}, \
                         {"assigns": "assigne"}, {"challenging homework": "devoirs difficiles"}, {"no prunes here": "pas de pruneaux ici"}, {"prune": "élaguer"}],

    "Spanish": [{"cloud": "nube"}, {"space": "espacio"}, {"assigns": "asigna"}, {"challenging homework": "tarea desafiante"}, {"no prunes here": "aquí no hay ciruelas pasas"}, {"prune": "ciruela pasa"}]
    }

f_translation = f'\nThe French translation of "{word.upper()}" is:\t'
s_translation = f'\nThe Spanish translation of "{word.upper()}" is:\t'

#French------------------------------------------------------------

if word == "cloud" and user_language == "French":
    print(f_translation, languages["French"][0]["cloud"])

elif word == "space" and user_language == "French":
    print(f_translation, languages["French"][1]["space"])

elif word == "assigns" and user_language == "French":
    print(f_translation, languages["French"][2]["assigns"])

elif word == "challenging homework" and user_language == "French":
    print(f_translation, languages["French"][3]["challenging homework"])

elif word == "no prunes here" and user_language == "French":
    print(f_translation, languages["French"][4]["no prunes here"])

elif word == "prune" and user_language == "French":
    print(f_translation, languages["French"][5]["prune"])

#Spanish------------------------------------------------------------

elif word == "cloud" and user_language == "Spanish":
    print(s_translation, languages["Spanish"][0]["cloud"])

elif word == "space" and user_language == "Spanish":
    print(s_translation, languages["Spanish"][1]["space"])

elif word == "assigns" and user_language == "Spanish":
    print(s_translation, languages["Spanish"][2]["assigns"])

elif word == "challenging homework" and user_language == "Spanish":
    print(s_translation, languages["Spanish"][3]["challenging homework"])

elif word == "no prunes here" and user_language == "Spanish":
    print(s_translation, languages["Spanish"][4]["no prunes here"])

elif word == "prune" and user_language == "Spanish":
    print(s_translation, languages["Spanish"][5]["prune"])

else:
    print(not_in_memory)