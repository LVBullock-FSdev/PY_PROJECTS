'''Laura V. Bullock
10/17/2024
Week7 - Day2
Homework3-translator.py

Rewrite the translation home using functions.'''

# Function to translate words
def translate(word, language):
    # Define an English words dictionary with translations for each language
    words = {
        "English": {
            "Jesus": {"french": "Jésus", "spanish": "Jesús", "Christ": "Jesus"},
            "Christ": {"french": "Christ", "spanish": "Cristo", "Christ": "Christus"},
            "cloud": {"french": "nuage", "spanish": "nube", "german": "Wolke"},
            "space": {"french": "espace", "spanish": "espacio", "german": "Raum"},
            "assigns": {"french": "assigne", "spanish": "asigna", "german": "weist zu"},
            "challenging": {"french": "difficiles", "spanish": "desafiante", "german": "herausfordernd"},
            "homework": {"french": "devoirs", "spanish": "tarea", "german": "Hausaufgaben"},
            "english": {"french": "anglaise(feminine), Anglais(masculine)", "spanish": "inglesa(feminine), inglés(masculine)", "german": "Englisch"},
            "purple": {"french": "violette(feminine), violet(masculine)", "spanish": "púrpura", "german": "lila"},
            "blue": {"french": "bleue(feminine), bleu(masculine)", "spanish": "azul", "german": "Blau"},
            "red": {"french": "rouge", "spanish": "roja(feminine), rojo(masculine)", "german": "Rot"},
            "yellow": {"french": "jaune", "spanish": "amarilla(feminine), amarillo(masculine)", "german": "Gelb"},
            "white": {"french": "blanche(feminine), blanc(masculine)", "spanish": "blanca(feminine), blanco(masculine)", "german": "Weiß"},
            "black": {"french": "noire(feminine), noir(masculine)", "spanish": "negra(feminine), negro(masculine)", "german": "Schwarz"},
            "brain": {"french": "cerveau", "spanish": "cerebro", "german": "Gehirn"},
            "apple": {"french": "pomme", "spanish": "manzana", "german": "Apfel"},
            "orange": {"french": "orange", "spanish": "naranja", "german": "orange"},
            "strawberry": {"french": "fraise", "spanish": "fresa", "german": "Erdbeere"},
            "prune": {"french": "élaguer", "spanish": "ciruela pasa", "german": "prune"},
            "water": {"french": "eau", "spanish": "agua", "german": "Wasser"},
            "watermelon": {"french": "pastèque", "spanish": "sandía", "german": "Wassermelone"},
            "class": {"french": "classe", "spanish": "clase", "german": "Klasse"},
            "sleepy": {"french": "somnolente(feminine), somnolent(masculine)", "spanish": "somnolienta(feminine), somnoliento(masculine)", "german": "schläfrig"},
            "headache": {"french": "mal de tête", "spanish": "dolor de cabeza", "german": "Kopfschmerzen"},
            "dictionary": {"french": "dictionnaire", "spanish": "diccionario", "german": "Wörterbuch"},
            "grandfather": {"french": "grand-père", "spanish": "abuelo", "german": "Großvater"},
            "grandmother": {"french": "grand-mère", "spanish": "abuela", "german": "Großmutter"},
            "father": {"french": "père", "spanish": "padre", "german": "Vater"},
            "mother": {"french": "mère", "spanish": "madre", "german": "Mutter"},
            "son": {"french": "fils", "spanish": "hijo", "german": "Sohn"},
            "daughter": {"french": "fille", "spanish": "hija", "german": "Tochter"},
            "family": {"french": "famille", "spanish": "familia", "german": "Familie"},
            "boy": {"french": "garçon", "spanish": "chico", "german": "Junge"},
            "girl": {"french": "fille", "spanish": "chica", "german": "Mädchen"},
            "dog": {"french": "chienne(feminine), chien(masculine)", "spanish": "perra(feminine), perro(masculine)", "german": "Hund"},
            "cat": {"french": "chatte(feminine), chat(masculine)", "spanish": "gata(feminine), gato(masculine)", "german": "Katze"}
        }
    }

    # Convert word to lowercase to match words keys
    word = word.lower()

    # Check if the word exists in the words
    if word in words["English"]:
        # Check if the translation for the selected language exists
        if language in words["English"][word]:
            print(f'The {language.upper()} translation for "{word}" is:\t', end="") #end="" to remove the return from the end of the line
            return words["English"][word][language]
    else:
        return f'Currently, "{word}" is not in memory.'

#Function to get user input and select the language
def language_translator():
    #Take the word input from the user
    word = input("\nEnter a word to translate: ")

    #Display language options
    print("\nSelect the language to translate to:")
    print("\t1. French")
    print("\t2. Spanish")
    print("\t3. German")

    #Get language choice input from the user
    choice = input("\nEnter the number of the language (1,2,3): ")

    #Conditions for user language choice
    if choice == '1':
        language = "french"
    elif choice == '2':
        language = "spanish"
    elif choice == '3':
        language = "german"
    else:
        return "Invalid language selection"

    #Calling the translate function to check for the word
    result=translate(word, language)
    # result =  f'\nThe {language.upper()} translation of "{word}" is: {translate(word, language)}\t'

    return result

#Calling the language_translator function
print(f"{language_translator()} \n\n\tThank you for playing.  Have a wonderfully blessed day!")
