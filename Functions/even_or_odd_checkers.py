'''Laura V. Bullock
10/17/2024
Week7 - Day2
Homework2-even_or_odd_checkers.py

Write code using function that will return even or return odd.'''

thanks = "Thank you for playing.  Have a wonderfully blessed day."
# Function to check if a number is even
def is_even(number):
    return number % 2 == 0  # True if even, False if odd

# Function to return whether the number is even or odd
def even_or_odd(number):
    if is_even(number):
        return f"{number} is an EVEN number.  {thanks}"
    else:
        return f"{number} is an ODD number.  {thanks}"
    
num = int(input(f"Please enter a whole number:\t"))

result = even_or_odd(num)
print(result)