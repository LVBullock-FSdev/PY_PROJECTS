'''Laura V. Bullock
10/21/2024
Week7 - Bonus Assignment

Write a Python program that will:
allow a user to guess the correct number. He/she will have 5 guesses. If user doesn't get it right after 5 guesses, print "you lose the game".
Give user input box: 
1. To capture guesses, he /she will choose number between 1 to 50, print message to tell user if guess is too high/low ,and let them know the rest of guesses remaining.
print(and input boxes)  If user wins  or If user loses

Tip:( remember you won't see  print statements during execution, so If you want to see prints during while loop, then print to the input box.

ALWAYS ASK YOURSELF THESE THREE QUESTIONS WHILE WORKING WITH LOOPS Three Loop Questions:
1. What do I want to repeat?
->
2. What do I want to change each time?
->
3. How long should we repeat?
->
'''

#Thes variables are global since being used in the different functions
thanks = f"\n\n Thank you for playing.  Have a wonderfully blessed day!"
player = input("\nWhose playing today?  Please enter your name:  ").upper()

#Prompt the user for a guess and show how many attempts are left
def get_user_guess(attempts_left):
    # Capture user guess and show how many attempts are left
    guess = int(input(f"Guess a number between 1 to 50. Attempts left: {attempts_left}\n\t Enter your guess here:   "))
    return guess

#
# checks the guess against my number and print whether the guess is too high, too low, or correct
def guess_checker(user_guess, my_number, attempts_left):
    # Check if guess is too high, too low, or correct
    if user_guess < my_number:
        print("\tToo LOW!  ", end="") #end="" to remove the return from the end of the line
        return False
    elif user_guess > my_number:
        print("\tToo HIGH!  ", end="")
        return False
    else:
        print(f"\n\t**********CONGRATULATIONS {player}, YOU HAVE WON THE GAME!!!*************\n\t\t   The correct number is:\t{my_number}  {thanks.upper()}")
        return True

#main loop, keep track of the attempts and exits if the user either wins or loses after 5 guesses
def guessing_game():
    # Set the correct number (hardcoded in this case, currently, not using random import)
    my_number = 45
    max_attempts = 5
    attempts_left = max_attempts
    
    print(f"\nWOO HOO, we've got a live one --> {player}'s on the game board today.\n\n WELCOME TO THE GUESSING GAME! You have {max_attempts} attempts to guess the correct number.\n")

    # Start at 5 and loop until 0 or user guesses the number
    while attempts_left > 0:
        user_guess = get_user_guess(attempts_left)
        
        if guess_checker(user_guess, my_number, attempts_left):
            return  # Exit if guessed correctly
        
        # Decrease the attempts left
        attempts_left -= 1  
        
        if attempts_left == 0:
            print(f"Sorry {player}, you lose! The correct number was {my_number}.  {thanks}")
        else:
            print(f"Try again! You have {attempts_left} guesses left.")
            
guessing_game()
