'''Laura V. Bullock
11/4/2024
Week8 - Day1
Homework2-sales-receipt_to_file.py

Write a code using functions that will add items in your grocery cart and return a total in a receipt text.
Order = {'tomato': 30, 'thyme':4.50, 'garlic':7.5, 'rice':10, 'onions':4, 'fish':9.99}
Add it to your GitHub ans send us a screenshot of your working code.'''

#Create a dictionary caller "Order"
Order = {
    'tomato': 30,
    'thyme': 4.5,
    'garlic': 7.5,
    'rice': 10,
    'onions': 4,
    'fish': 9.99}

def grocery_cart(order):
    cart = []
    total = 0
    draw_line = "*" * 35 + "\n"

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

grocery_cart(Order)

print("Your receipt was emailed to you as 'super_bolt_groceries_receipt.txt'")