'''Laura V. Bullock
11/7/2024
Week8 - Day1
Homework2-sales-receipt_to_file.py

Write a code using functions that will add items in your grocery cart and return a total in a receipt text.
Order = {'tomato': 30, 'thyme':4.50, 'garlic':7.5, 'rice':10, 'onions':4, 'fish':9.99}
Add it to your GitHub ans send us a screenshot of your working code.'''

def grocery_cart(order):
    """
        Add items to a grocery cart and return a total in a receipt text..

        Args:
            Order (dictionary): A dictionary with product and price.
            cart (list): items from Order to be added to the cart.
        
        Returns:
            The product of all even numbers in the list or 
            

        Raises:
            ValueError: If Order is empty; therefore cart is empty.
            TypeError: If the input is an invalid dictionary type.
            NameError: If a value is not defined.
        """

    cart = []
    total = 0
    draw_line = "*" * 35 + "\n"

    # Check if there is anything in the dictionary
    if not Order:
        raise ValueError("NO VALUES ENTERED; THERFORE THE CART IS EMPTY.")
    
    #Add products to products_purchased dictionary and calculate total
    for product, price in order.items():
        cart.append((product, price))
        total += price

    #Generate a receipt as a text file
    with open('super_bolt_groceries_receipt.txt', 'w') as receipt:
        receipt.write("\nWelcome to Super Bolt Grocery Center\n\n")
        receipt.write(f"\tReceipt for your groceries:\n{draw_line}")
        for product, price in cart:
            receipt.write(f"\t{product}:\t\t${price:.2f}\n")
        receipt.write(f"{draw_line}\tTotal:\t\t${total:.2f}\n")
        receipt.write("\nThanks for shopping with us today. \nHAVE A WONDERFULLY BLESSED DAY!\n")

try:
    #Create a dictionary called "Order"
    Order = {
        'tomato': 30,
        'thyme': 4.5,
        'garlic': 7.5,
        'rice': 10,
        'onions': 4,
        'fish': 9.99}

#Examples for try except
    
    # ValueError (no values, empty dictionary)
    #Order = {}

    # TypeError (price contains a string)
    '''Order = {
        'tomato': 30,
        'thyme': 4.5,
        'garlic': 7.5,
        'rice': 10,
        'onions': '4',
        'fish': 9.99}'''

    # NameError (value not defined)
    '''Order = {
        'tomato': 30,
        'thyme': 4.5,
        'garlic': 7.5,
        'rice': 10,
        'onions': c,
        'fish': 9.99}'''

except TypeError as error:
    raise TypeError(f"AN ERROR HAS OCCURRED:  {error}")
except NameError as e:
    raise NameError(f"VALUE NOT DEFINED: {e}")

print("Your receipt was emailed to you as 'super_bolt_groceries_receipt.txt'")

grocery_cart(Order)