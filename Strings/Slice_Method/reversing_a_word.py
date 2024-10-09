'''CLOUDSPACE ACADEMY
Python-AWS/August 2024
Instructor:  Cloudio Sidi

Laura V. Bullock
9/20/2024
Week3 Day2 
Lab4-reversing_a_word.py

Write a program that will ask for a word as reverse the word.

Display on the screen: Your word is: word, and the reverse is: reverse_word.

Leverage methods: split, join and reversed.'''

word = input("Please enter a word:\t")
reversed_word = word[::-1]
# reversed_word = reversed(word) #returns object location 
# split, join and reversed methods seem to be used for sentences.

print(f"Your word is: {word}, and the reverse is: {reversed_word}.")
print(f"There is a {reversed_word} in using Python.")