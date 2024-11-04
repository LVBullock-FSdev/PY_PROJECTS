'''Laura V. Bullock
11/4/2024
Week8 - Day1
Homework2-sales.py

Write a code using functions that will add items in your grocery cart and return a total in a receipt text.

Order = {'tomato': 30, 'thyme':4.50, 'garlic':7.5, 'rice':10, 'onions':4, 'fish':9.99}

Add it to your GitHub ans send us a screenshot of your working code.'''

# Define the order dictionary
Order = {'tomato': 30, 'thyme': 4.50, 'garlic': 7.5, 'rice': 10, 'onions': 4, 'fish': 9.99}

# Function to calculate total and generate receipt text
def generate_receipt(Order):
    #Get the sum of all values in order dictionary
    total = sum(Order.values())
    #Generate a separation line for the receipt
    draw_line = "*" * 30 + "\n"
    #Text to be printed on the receipt
    receipt = f"\nThank you for shopping with us today.\n\nYour Receipt is printed below:\n{draw_line}"

    #Get the each product and price then add to the receipt
    for product, price in Order.items():
        receipt += f"\t{product.capitalize()}:  ${price:.2f}\n"

    receipt += f"{draw_line}\n\tTotal: \t${total:.2f}\n\nHAVE A WONDERFULLY BLESSED DAY!"

    return receipt

# Print the receipt
print(generate_receipt(Order))