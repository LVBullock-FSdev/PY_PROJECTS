'''
Laura V. Bullock
11/12/2024
Week12 - Day1 - Develop on AWS
In-Class Exercise-create_file_2-s3.py

Write a function to create a text file called python-on-aws.txt, write on the file the text below: "programming is fun, but you got to practice". Write another the function to upload the file created previously to any existing S3 bucket on AWS.
'''

import boto3

# function to create a text file called python-on-aws.txt
def create_text_file():

    """
    Creates a text file called python-on-aws.txt with the text "programming is fun, but you got to practice".

    Args:
        file_name (string): name of the file.
    
    Returns:
        The file name 
    """
    
    # Create a text file and write the specified text to it
    file_name = "python-on-aws.txt"
    with open(file_name, "w") as file:
        file.write("Programming is fun, but you must practice!!!")
    print(f'"{file_name}" created successfully.')
    return file_name

def upload_to_s3(file_name, bucket_name):
    """
    Uploads the "python-on-aws.txt" file created in create_text_file() to an existing S3 bucket on AWS.

    Args:
        s3_client(boto3.client("s3"): name of AWS service accessed using boto3.
    
    Raises:
        FileNotFoundError: If the system is unable to find the file.
        Exception: If any other error occurs.
    """
    # Initialize the S3 client
    s3_client = boto3.client("s3")
    
    # Upload create_file_2_s3.txt to cloudspace-lvb
    try:
        s3_client.upload_file(file_name, bucket_name, file_name)
        print(f'"{file_name}" successfully uploaded to "{bucket_name}" bucket.')
    except FileNotFoundError:
        print(f'FileNotFoundError: "{file_name}" was not found!!')
    except Exception as e:
        print(f"Error uploading file: {e}")

# Main
file_name = create_text_file()
bucket_name = "cloudspace-lvb"  # my bucket name
upload_to_s3(file_name, bucket_name)