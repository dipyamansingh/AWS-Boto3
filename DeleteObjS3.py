import boto3
client = boto3.client('s3')

response = client.delete_object(
    Bucket='mickutest1',
    Key='create_bucket.py'
)
