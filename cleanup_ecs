import boto3

def lambda_handler(event, context):
    ecs = boto3.client('ecs')
    
    # Get all ECS clusters
    response = ecs.list_clusters()

    # Iterate through each cluster
    for cluster_arn in response['clusterArns']:
        services = ecs.list_services(cluster=cluster_arn)['serviceArns']
        tasks = ecs.list_tasks(cluster=cluster_arn)['taskArns']
        if not services and not tasks:
            ecs.delete_cluster(cluster=cluster_arn)
            print(f"Deleted ECS Cluster {cluster_arn}.")

    return {
        'statusCode': 200,
        'body': 'ECS Cluster cleanup complete'
    }
