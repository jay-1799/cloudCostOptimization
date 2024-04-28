import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # Get all EC2 instances
    response = ec2.describe_instances()

    # Iterate through each instance
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            # Check if the instance name contains 'Production'
            if 'Name' in instance:
                instance_name = instance['Name']
                if 'Production' in instance_name:
                    # Tag instance as Production environment
                    ec2.create_tags(Resources=[instance_id], Tags=[{'Key': 'Environment', 'Value': 'Production'}])
                    print(f"Tagged EC2 Instance {instance_id} with 'Environment: Production'.")
            else:
                # Tag instance as Development environment if instance name is not available
                ec2.create_tags(Resources=[instance_id], Tags=[{'Key': 'Environment', 'Value': 'Development'}])
                print(f"Tagged EC2 Instance {instance_id} with 'Environment: Development'.")

    return {
        'statusCode': 200,
        'body': 'Resource tagging complete'
    }
