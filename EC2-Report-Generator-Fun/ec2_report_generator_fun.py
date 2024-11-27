'''Laura V. Bullock
11/24/2024
Week13 - Day1 - EC2 Report Generator Fun
Homework1-ec2_report_generator_fun.py

HOMEWORK: @channel :alert:
Due: 11/26/2024
1. Repurpose the list_all_ec2_instances() to return a dictionary containing keyname: instance_name, instance_type, image_id, state
2. repurpose generate_csv_report to use DictWriter method
3. write a function to email yourself and CC cloudspace at info@cloudspaceacademy.com. If possible attach the report or send the s3 bucket link. Use AWS services'''

import boto3
import csv
import botocore
import logging
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
    This function will gather all of Laura's ec2 instances
    :param
    lauras_ec2_instances = [an empty list]
    :return
    a dictionary of instances
    """
    # create an empty list to store the details of the instances
    lauras_ec2_instances = []

    # Initialize the ec2 client
    ec2_client = boto3.client('ec2')

    # Gets the details of all of the EC2 instances as a response
    #resource:  https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_instances.html
    response = ec2_client.describe_instances()

    # Looping through the reservations and extract the details
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            # Get the instance name (from tags, if available)
            instance_name = ''
            for tag in instance.get('Tags', []):
                if tag['Key'] == 'Name':
                    instance_name = tag['Value']
                    break

            # Creating a dictionary with the instance details
            instance_details = {
                'instance_name': instance_name,
                'instance_type': instance['InstanceType'],
                'image_id': instance['ImageId'],
                'state': instance['State']['Name']
            }
            lauras_ec2_instances.append(instance_details)

            # print(lauras_ec2_instances)
    return lauras_ec2_instances

# Repurpose generate_csv_report to use DictWriter method
def generate_csv_report(instances):
    """
        This function will generate a csv report per Micheal
        :param list of instances
        :return return true if valid
    """
    try:
        #resource:  https://docs.python.org/3/library/csv.html
        with open(REPORT_NAME, 'w', newline='') as csvfile:
            fieldnames = ['instance_name', 'instance_type', 'image_id', 'state']
            csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # Write the header row
            csvwriter.writeheader()
            # Write the details of the instances
            csvwriter.writerows(instances)

    except FileNotFoundError:
        print(f'FileNotFoundError: "{REPORT_NAME}" was not found!!')
    except Exception as e:
        print(f"Error uploading file: {e}")
        return False
    return True # optional

def upload_report_to_s3():
    """
        This function will upload csv report to s3 bucket
        :param 
        :return 
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
    <h3>According to https://docs.aws.amazon.com/ses/latest/dg/send-email-raw.html, this is how to send an email via AWS SES.  The EC2 Report is attached for your review</h3>
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
        print(f"Error sending email: {error}")

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