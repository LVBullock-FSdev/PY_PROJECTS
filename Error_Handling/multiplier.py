'''Laura V. Bullock
10/4/2024
Week9 - Day1 - Error Handling
Homework1-multiplier.py

Write a function called multiply_even_numbers that accepts a list of numbers and returns the product of all even numbers in the list.

Numbers = [8, 9, 11, 20, 32, 101, 100]

Please have exceptions handled and docstrings.  Add it to your GitHub and send us screenshot of working code.'''

# Function to multiply all even numbers and return the product
def multiply_even_numbers(numbers):
    """
    Multiplies all even numbers in a list and returns the product.

    Args:
        numbers (list[int]): A list of integers.
    
    Returns:
        The product of all even numbers in the list or 
        ValueError: If no even numbers are found or the list is empty.

    Raises:
        TypeError: If the data sequence type is a not a list or if a number is not an integer.
    """

    #Check if data sequence type is a list (whether the variable numbers is an instance of the list class) - using isinstance
    #source: https://www.w3schools.com/python/ref_func_isinstance.asp or https://tutorpython.com/2-ways-to-check-if-variable-is-a-list-in-python/ or https://www.geeksforgeeks.org/python-check-if-a-given-object-is-list-or-not/
    if not isinstance(numbers, list):
        raise TypeError("INVALID DATA SEQUENCE TYPE:  expecting a LIST.")
    
    #Initialize product and even numbers to False
    product = 1
    even_nums_found = False

    try:
        for num in numbers:
            #Multiply only even numbers
            if num % 2 == 0:
                product *= num
                #Check for even numbers
                even_nums_found = True

    except TypeError:
        raise TypeError("ALL VALUES MUST BE INTEGERS.")

    #Return ValueError if no even numbers were found or if list is empty
    return product if even_nums_found else ValueError("ValueError:  NO EVEN NUMBERS FOUND.")

try:
    numbers = [8, 9, 11, 20, 32, 101, 100]
    #Examples for try except:
    #numbers = [8, 9, 11, 20, 32, 101, b, 100] # - NameError
    #numbers = {8, 9, 11, 20, 32, 101, 100} # - TypeError - data sequence type not a list
    #numbers = [8, "9", 11, 20, 32, 101, 100] # - TypeError 
    #numbers = [1, 3, 5, 7] # - ValueError
    #numbers = [] # - ValueError

except NameError as e:
    raise NameError(f"VALUE NOT DEFINED: {e}")

result = multiply_even_numbers(numbers)

print(f"Output:  {result}")