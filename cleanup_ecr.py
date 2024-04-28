import boto3
from datetime import datetime, timedelta

def lambda_handler(event, context):
    ecr = boto3.client('ecr')
    
    # Get all ECR repositories
    response = ecr.describe_repositories()

    # Define retention period (7 days)
    retention_period = datetime.now() - timedelta(days=7)
    
    # Iterate through each repository
    for repo in response['repositories']:
        images = ecr.list_images(repositoryName=repo['repositoryName'])['imageIds']
        if not images and repo['createdAt'] < retention_period:
            ecr.delete_repository(repositoryName=repo['repositoryName'], force=True)
            print(f"Deleted ECR Repository {repo['repositoryName']}.")

    return {
        'statusCode': 200,
        'body': 'ECR Repository cleanup complete'
    }
