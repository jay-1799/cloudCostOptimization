import boto3

def lambda_handler(event, context):
    eks = boto3.client('eks')
    
    # Get all EKS clusters
    response = eks.list_clusters()

    # Iterate through each cluster
    for cluster_name in response['clusters']:
        fargate_profiles = eks.list_fargate_profiles(clusterName=cluster_name)['fargateProfileNames']
        nodegroups = eks.list_nodegroups(clusterName=cluster_name)['nodegroups']
        if not fargate_profiles and not nodegroups:
            eks.delete_cluster(name=cluster_name)
            print(f"Deleted EKS Cluster {cluster_name}.")

    return {
        'statusCode': 200,
        'body': 'EKS Cluster cleanup complete'
    }
