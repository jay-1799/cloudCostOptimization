import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # Get all EBS volumes
    response = ec2.describe_volumes()

    # Iterate through each volume
    for volume in response['Volumes']:
        if not volume['Attachments']:
            ec2.delete_volume(VolumeId=volume['VolumeId'])
            print(f"Deleted EBS Volume {volume['VolumeId']}.")

    return {
        'statusCode': 200,
        'body': 'EBS Volume cleanup complete'
    }
