import boto3
from datetime import datetime, timedelta

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # Get all elastic IP addresses
    response = ec2.describe_addresses()

    # Define retention period (7 days)
    retention_period = datetime.now() - timedelta(days=7)
    
    # Iterate through each elastic IP address
    for address in response['Addresses']:
        if 'AssociationId' not in address and address['AllocationTime'] < retention_period:
            ec2.release_address(AllocationId=address['AllocationId'])
            print(f"Released Elastic IP Address {address['PublicIp']}.")

    return {
        'statusCode': 200,
        'body': 'Elastic IP cleanup complete'
    }
