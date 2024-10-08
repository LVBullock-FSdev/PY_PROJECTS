'''Laura V. Bullock
10/4/2024
Week5 - Day2
Homework-optional_language_translator.py

- Create an English to French translator program.
- The programs takes a word from the user as an input and translates it using a dictionary data type as a vocabulary word.
- Please add the translation of "prune" in your homework.
- If the word is not in the French code, print "[word]" is not in memory)
***The user will select the language that he/she would like to translate to*** (optional)

------------------------***OPTIONAL***--------------------------------
***The user will select the language in which to translate the word to*** (optional)'''


# creating a dictionary which holds the English word as the key and the value of the specific language
languages = {
    "French": {"cloud": "nuage", "space": "espace", "assigns": "assigne", "challenging":  "difficiles", "homework": "devoirs", "no prunes here": "pas de pruneaux ici", "prune": "élaguer"},

    "Spanish": {"cloud": "nube", "space": "espacio", "assigns": "asigna", "challenging": "desafiante", "homework": "tarea", "no prunes here": "aquí no hay ciruelas pasas", "prune": "ciruela pasa"},

    "German": {"cloud": "Wolke", "space": "Raum", "assigns": "weist zu", "challenging": "herausfordernd", "homework": "Hausaufgaben", "no prunes here": "hier gibt es keine Pflaumen", "prune": "beschneiden OR kürzen OR stutzen"}
    }

print(languages)

#prompt user to enter a word
word = input('\nPlease enter a word here-->   ')

#prompt user to enter a language
user_language = input('\nPlease enter a your preferred language here-->   ')

#get the relevant word from the languages dictionary
f_translation = languages["French"].get(word)
s_translation = languages["Spanish"].get(word)
g_translation = languages["German"].get(word)

french_msg = f'\nThe French translation of "{word}" is:\t'
spanish_msg = f'\nThe Spanish translation of "{word}" is:\t'
german_msg = f'\nThe German translation of "{word}" is:\t'

if not word and not user_language:
    print(f'\nOops, you have no entries.  Please try again.')
elif not word:
    print(f'\nOops, you have not entered a word.  Please try again.')
elif not user_language:
    print(f'\nOops, you have not entered a language.  Please try again.')
elif not f_translation or not s_translation or not s_translation:
    print(f'\nOops currently, the word "{word}" is not in memory, but we can add it in the future provided it is a real word.')

elif user_language == "French":
    print(french_msg, f_translation)

elif user_language == "Spanish":
    print(spanish_msg, s_translation)

elif user_language == "German":
    print(german_msg, g_translation)

else:
    print(f'Oops, currently, the {user_language.upper()} translation of "{word}" not in memory.')