'''Laura V. Bullock
10/4/2024
Week5 - Day2
Homework-english_french_translator.py

- Create an English to french translator program.
- The programs takes a word from the user as an input and translates it using a dictionary data type as a vocabulary word.
- Please add the translation of "prune" in your homework.
- If the word is not in the French code, print "[word]" is not in memory)
***The user will select the language that he/she would like to translate to*** (optional)
'''

# declare an empty dictionary
french = {}

#Add to the dictionary
french["Jesus"] = "Jésus"
french["Christ"] = "Christ"
french["cloud"] = "nuage"
french["space"] = "espace"
french["assigns"] = "assigne"
french["challenging"] = "difficiles"
french["homework"] = "devoirs"
french["no prunes here"] = "pas de pruneaux ici"
french["english"] = "anglaise(feminine), Anglais(masculine)"
french["purple"] = "violette(feminine), violet(masculine)"
french["brain"] = "cerveau"
french["apple"] = "pomme"
french["orange"] = "orange"
french["strawberry"] = "fraise"
french["prune"] = "élaguer"
french["water"] = "eau"
french["watermelon"] = "pastèque"
french["class"] = "classe"
french["sleepy"] = "somnolente(feminine), somnolent(masculine)"
french["headache"] = "mal de tête"
french["dictionary"] = "dictionnaire"
french["father"] = "père"
french["mother"] = "mère"
french["son"] = "fils"
french["daughter"] = "fille"
french["family"] = "famille"
french["boy"] = "garçon"
french["girl"] = "fille"
french["dog"] = "chienne(feminine), chien(masculine)"
french["cat"] = "chatte(feminine), chat(masculine)"

#Print the dictionary
print(french)

#get user input
user_input = input('\nPlease enter a word here-->   ')

#declaration for word not in memory
not_in_memory = f'\nSorry, the word "{user_input.upper()}" is not in memory today, but we can add it in the future if it is a real word.'

result_msg = f'\nThe French translation of "{user_input.upper()}" is:\t'

french_translation = french.get(user_input)

#Condition to check for word and print a result
if french_translation:
    print(result_msg, french_translation)
else:
    print(not_in_memory)