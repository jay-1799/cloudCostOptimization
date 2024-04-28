import boto3
import datetime

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # Get current day of the week (0 = Monday, 6 = Sunday)
    current_day = datetime.datetime.today().weekday()

    # Check if it's a weekend (Saturday or Sunday)
    if current_day == 5 or current_day == 6:
        # Get all EC2 instances
        response = ec2.describe_instances()

        # Iterate through each instance
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                # Check if the instance is tagged as 'development'
                for tag in instance.get('Tags', []):
                    if tag['Key'] == 'Environment' and tag['Value'] == 'development':
                        instance_id = instance['InstanceId']
                        # Stop the instance
                        ec2.stop_instances(InstanceIds=[instance_id])
                        print(f"Stopped EC2 Instance {instance_id}.")

        return {
            'statusCode': 200,
            'body': 'Resource shutdown complete'
        }
    else:
        return {
            'statusCode': 200,
            'body': 'Not a weekend, no action taken'
        }
