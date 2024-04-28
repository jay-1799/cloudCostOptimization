import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Define the tag key and value to identify instances for termination
    tag_key = 'Environment'
    tag_value = 'Testing'

    # Get all EC2 instances with the specified tag
    response = ec2.describe_instances(Filters=[{'Name': f'tag:{tag_key}', 'Values': [tag_value]}])

    # Iterate through each instance and terminate it
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            ec2.terminate_instances(InstanceIds=[instance_id])
            print(f"Terminated EC2 Instance {instance_id}.")

    return {
        'statusCode': 200,
        'body': 'EC2 instance termination complete'
    }
