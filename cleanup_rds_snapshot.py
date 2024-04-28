import boto3
from datetime import datetime, timedelta

def cleanup_rds_snapshots():
    rds = boto3.client('rds')

    # Get all RDS snapshots
    response = rds.describe_db_snapshots()

    # Define a retention period (e.g., 7 days)
    retention_period_days = 7
    retention_cutoff = datetime.now() - timedelta(days=retention_period_days)

    # Iterate through each snapshot and delete if older than the retention period
    for snapshot in response['DBSnapshots']:
        snapshot_id = snapshot['DBSnapshotIdentifier']
        snapshot_create_time = snapshot['SnapshotCreateTime'].replace(tzinfo=None)

        if snapshot_create_time < retention_cutoff:
            rds.delete_db_snapshot(DBSnapshotIdentifier=snapshot_id)
            print(f"Deleted RDS snapshot {snapshot_id} created on {snapshot_create_time}.")

# cleanup_rds_snapshots()
