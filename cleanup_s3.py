import boto3
from datetime import datetime, timedelta

def cleanup_s3_bucket(bucket_name):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)

    # Define a retention period (e.g., 30 days)
    retention_period_days = 30
    retention_cutoff = datetime.now() - timedelta(days=retention_period_days)

    # Iterate through each object and delete if last modified before the retention cutoff
    for obj in bucket.objects.all():
        last_modified = obj.last_modified.replace(tzinfo=None)

        if last_modified < retention_cutoff:
            obj.delete()
            print(f"Deleted S3 object {obj.key} last modified on {last_modified}.")


# cleanup_s3_bucket('your_bucket_name')
