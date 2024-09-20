'''CLOUDSPACE ACADEMY
Python-AWS/August 2024
Instructor:  Cloudio Sidi

Laura V. Bullock
9/20/2024
Week3 Day2 
Lab3-aws_account_id.py

Write a program that will display the account id from the arn below:
arn:aws:iam::123456789012:user/Development/product_1234/*

Display on the screen: the aws account id is: account_id.'''

arn = "aws:iam::123456789012:user/Development/product_1234/*"
account_id = arn[9:21]
print(f"The aws account id is: {account_id}.")