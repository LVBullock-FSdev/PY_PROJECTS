'''
Laura V. Bullock
11/14/2024
Week12 - Day2 - Develop on AWS
In-Class Exercise-create_ec2_instance.py

Write a function to create an EC2 LINUX instance with the name ec2-created-by-python.
- Provide an Amazon Linux 2 AMI
- Use t3.micro instance type
Use all the best practices, handle exception, use variables, use main, doc strings etc….
'''

import boto3
import logging

# Configure logging
logging.basicConfig(filename='create_ec2_instance.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

def create_ec2_instance():
    """
    Create an EC2 instance with the name 'ec2-created-by-python' in AWS.
    Uses the default AMI, instance type.

    Args:
        ami_id (string): the id of the ami found in AWS console.
        instance_type (string): type of instance to be created.
        security_group_id (string): security group id
        instance_name (string): name of the instance.
        monitoring (dict): Enabled: True
    
    Returns:
        Response as created instance id on the "Instances" page of AWS Console and launches the instance.

    Raise:
        Exception as error if failed to create the instance. 
    """
    
    # Variables
    ami_id = "ami-0984f4b9e98be44bf"  # Provide an Amazon Linux 2 AMI - This is the ImageID
    instance_type = "t3.micro"  # Use t3.micro instance type
    security_group_id = "sg-0fc15011e8a1fefb1"  # Will add to default if not specified
    instance_name = "ec2-created-by-python-11/26/2024"
    monitoring = {'Enabled': True}
    
    # Initialize the EC2 client
    ec2_client = boto3.client("ec2")

    try:
        # Launch a new EC2 instance and start it using run_instances
        response = ec2_client.run_instances(
            ImageId = ami_id,
            InstanceType = instance_type,
            SecurityGroupIds = [security_group_id],
            MinCount = 1,
            MaxCount = 1,
            Monitoring = monitoring,
            #The following allows instance name to appear, see documentation --> https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/run_instances.html#:~:text=TagSpecifications%3D%5B,%5D%0A%20%20%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%5D%2C
            TagSpecifications = [
                {
                    "ResourceType": "instance",
                    #On the Instances page, Key is Name which is the header name and Value is the name you gave the instance, ie. instance_name variable above
                    "Tags": [{"Key": "Name", "Value": instance_name}]
                }
            ]
        )
        
        instance_id = response["Instances"][0]["InstanceId"]
        print(f'EC2 Instance created with ID: {instance_id} as "{instance_name}."')

        logger.info(f'EC2 Instance created with ID: {instance_id} as "{instance_name}."')
        return response["Instances"][0]
    
    except Exception as e:
        logger.error(f"Failed to create EC2 instance: {e}")
        return f"Error: {e}"

if __name__ == "__main__":
    instance_info = create_ec2_instance()
    if instance_info:
        logger.info(f"Successfully created an EC2 instance.  See info below:\n {instance_info}")
    else:
        logger.error("Failed to create EC2 instance")

    logger.info(f"End of the log! \n" + "*" * 60)