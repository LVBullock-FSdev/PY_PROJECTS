import boto3

#Verify email addresses
def verify_email(email_address):

    '''
    This function will verify an email address on AWS SES servise

    arg:
    ses_client
    '''
    # Create a client for Amazon SES
    ses_client = boto3.client('ses', region_name='us-east-1')  # Change region as necessary
    
    try:
        # Request email verification
        response = ses_client.verify_email_identity(EmailAddress=email_address)
        print(f"Verification email sent to {email_address}. Response: {response}")
    except Exception as e:
        print(f"Error verifying email {email_address}: {e}")

email_to_verify = "codelily86@gmail.com"

#call the function
verify_email(email_to_verify)