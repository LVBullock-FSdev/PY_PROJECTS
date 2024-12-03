'''Laura V. Bullock
12/03/2024
Week13 - Day1 - EC2 Report Generator with Dictionary
Homework1-ec2_report_generator_using_dictionary.py

HOMEWORK: @channel :alert:
Due: 12/03/2024
1. Repurpose the list_all_ec2_instances() to return a dictionary containing keyname: instance_name, instance_type, image_id, state
2. repurpose generate_csv_report to use DictWriter method
3. write a function to email yourself and CC cloudspace at info@cloudspaceacademy.com. If possible attach the report or send the s3 bucket link. Use AWS services'''

import boto3
import csv
import botocore
import logging
import json
from botocore.exceptions import BotoCoreError, ClientError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

#Configure logging
logging.basicConfig(filename='EC2_Report_Generator_Fun.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

# global var
REPORT_NAME = 'lauras_ec2_report.csv'
CLOUDSPACE_BUCKET = 'cloudspace-lvb'

# Repurpose the list_all_ec2_instances() to return a dictionary containing keyname: instance_name, instance_type, image_id, state
def list_all_lauras_ec2_instances():
    """
    Retrieve EC2 instance information and return it as a dictionary.
    """
    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_instances()
    
    instances_info = {}
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            # Extract information
            instance_id = instance.get('InstanceId', 'Unknown')
            instance_name = 'Unknown'
            for tag in instance.get('Tags', []):
                if tag['Key'] == 'Name':
                    instance_name = tag['Value']
            instance_type = instance.get('InstanceType', 'Unknown')
            image_id = instance.get('ImageId', 'Unknown')
            state = instance['State']['Name']
            
            # Add to dictionary
            instances_info[instance_id] = {
                'Name': instance_name,
                'Type': instance_type,
                'Image': image_id,
                'State': state
            }
    
    return instances_info

# Repurpose generate_csv_report to use DictWriter method
def generate_csv_report(instances):
    """
        This function will generate a CSV file with EC2 instance information using the csv DictWriter method.

        Args:
            instances = list_all_lauras_ec2_instances()
            dictionary: {Instance ID': instance_id,
                        'Name': details['Name'],
                        'Type': details['Type'],
                        'Image': details['Image'],
                        'State': details['State']} containing details of ec2 instances
        Returns:
            return true if valid

        Raises:
            FileNotFoundError: If the system is unable to find the file.
            Exception: If error occurs with uploading the file.
    """
    instances = list_all_lauras_ec2_instances()
    try:
        #resource:  https://docs.python.org/3/library/csv.html
        with open(REPORT_NAME, 'w', newline='') as csvfile:
            fieldnames = ['Instance ID', 'Name', 'Type', 'Image', 'State']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for instance_id, details in instances.items():
                writer.writerow({
                    'Instance ID': instance_id,
                    'Name': details['Name'],
                    'Type': details['Type'],
                    'Image': details['Image'],
                    'State': details['State']
                })

    except FileNotFoundError:
        print(f'FileNotFoundError: "{REPORT_NAME}" was not found!!')
    except Exception as e:
        print(f"Error uploading file: {e}")
        return False
    return True # optional

def upload_report_to_s3():
    """
        This function will upload csv report to s3 bucket
        Args:
            s3_client(boto3.client("s3"): name of AWS service accessed using boto3.
        Raises:
            botocore.exceptions.ClientError:  If error uploading file 
    """
    
    s3_client = boto3.client('s3')

    try:
        s3_client.upload_file(REPORT_NAME, CLOUDSPACE_BUCKET, REPORT_NAME)
    except botocore.exceptions.ClientError as error:
        logger.error(f"An error occurred while uploading the file: \n{error}")

# Write a function to email yourself and CC cloudspace at info@cloudspaceacademy.com. If possible attach the report or send the s3 bucket link. Use AWS services
def send_email_with_attachment_using_ses():
    """
        This function will send an email to myself and CC cloudspace at info@cloudspaceacademy.com with the ec2 report csv attachment.
        Args:
            - sender
            - recipient
            - cc
            - subject
            - attachment
            - body_text
            - body_html
            - CHARSET
            - msg
            ses_client = boto3.client('sesv2') name of AWS email service accessed using boto3.
        
        :return 
    """

    SENDER = "Laura Bullock <wonderwoman.codes@gmail.com>"
    RECIPIENT = "wonderwoman.codes@gmail.com"
    CC = "codelily86@gmail.com"
    # CONFIGURATION_SET = "ConfigSet" # <<--- what is this?
    # AWS_REGION = "us-east-1"  #<< -- where is this being used?
    SUBJECT = "EC2 Report CSV file"
    ATTACHMENT = "lauras_ec2_report.csv"
    BODY_TEXT = "Hello,\r\n Sending an email with an attachment using AWS SES."

    # The HTML body of the email.
    BODY_HTML = """\
    <html>
    <head/>
    <body>
    <h1>Hello Cloudio!</h1>
    <h3>According to https://docs.aws.amazon.com/ses/latest/dg/send-email-raw.html, this is how to send an email via AWS SES.  The EC2 Report is attached for your review.  I enlisted the help of ChatGPT and was finally able to get it work properly.  However, I was unable to get it to automatically verify an email, though.  Perhaps you can show us that in class.</h3>
    <h3>I pray that you and your family had a wonderfully blessed Thanksgiving celebration together.</h3>
    </body>
    </html>
    """

    # The character encoding for the email.
    CHARSET = "utf-8"
    msg = MIMEMultipart('mixed')
    # Add subject, from and to lines.
    msg['Subject'] = SUBJECT 
    msg['From'] = SENDER 
    msg['To'] = RECIPIENT
    msg['cc'] = CC
    
    # Create a multipart/alternative child container.
    msg_body = MIMEMultipart('alternative')
    
    # Encode the text and HTML content and set the character encoding. This step is
    # necessary if you're sending a message with characters outside the ASCII range.
    textpart = MIMEText(BODY_TEXT.encode(CHARSET), 'plain', CHARSET)
    htmlpart = MIMEText(BODY_HTML.encode(CHARSET), 'html', CHARSET)
    
    # Add the text and HTML parts to the child container.
    msg_body.attach(textpart)
    msg_body.attach(htmlpart)
    
    # Define the attachment part and encode it using MIMEApplication.
    att = MIMEApplication(open(ATTACHMENT, 'rb').read())
    
    # Add a header to tell the email client to treat this part as an attachment,
    # and to give the attachment a name.
    att.add_header('Content-Disposition','attachment',filename=os.path.basename(ATTACHMENT))
    
    # Attach the multipart/alternative child container to the multipart/mixed
    # parent container.
    msg.attach(msg_body)
    msg.attach(att)

    #changes start from here
    strmsg = str(msg)
    body = bytes (strmsg, 'utf-8')

    ses_client = boto3.client('sesv2')

    try:
        response = ses_client.send_email(
        FromEmailAddress=SENDER,
        Destination={
            'ToAddresses': [RECIPIENT],
            'CcAddresses': [CC]
        },
        Content={
            'Raw': {
                'Data': body
            }
        }
        )
        print(f'Email successfully sent to {RECIPIENT} and {CC}!')

        logger.info(f'Message ID: {response["MessageId"]}\n {response}')

    except (BotoCoreError, ClientError) as error:
        logger.error(f"Error sending email: {error}")

#main
if __name__ == '__main__':

    #call function
    instances = list_all_lauras_ec2_instances()

    logger.info(f'Successfully generated csv report as {REPORT_NAME}')
    # generate report
    generate_csv_report(instances)

    logger.info(f'{REPORT_NAME} successfully uploaded to {CLOUDSPACE_BUCKET}')
    # upload report
    upload_report_to_s3()

    send_email_with_attachment_using_ses()

    logger.info(f"End of the log! \n" + "*" * 60)