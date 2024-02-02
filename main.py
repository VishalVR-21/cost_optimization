import boto3
from datetime import datetime, timedelta



def fetch_s3_bucket_details(aws_access_key_id, aws_secret_access_key, aws_region=None):
    # Create an S3 client with explicit credentials
    s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id,
                             aws_secret_access_key=aws_secret_access_key,
                             region_name=aws_region)

    try:
        # List all S3 buckets
        response = s3_client.list_buckets()

        # Print bucket details
        print("S3 Buckets:")
        for bucket in response['Buckets']:
            print(f" - {bucket['Name']}")
            print(f"   Created: {bucket['CreationDate']}")
            print()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace with your actual AWS credentials and region
    aws_access_key_id = 'AKIARYIR2WD54MOFL6I5 '
    aws_secret_access_key = 'rHYFWpw5yIjPfspe27fjiOJl0qOuHFt5cBuCltDi'

    fetch_s3_bucket_details(aws_access_key_id, aws_secret_access_key)