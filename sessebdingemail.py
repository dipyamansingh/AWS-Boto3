import boto3
client = boto3.client(
    'ses',
    region_name=region,
    aws_access_key_id='aws_access_key_string',
    aws_secret_access_key='aws_secret_key_string'
)
response = client.send_email(
    Destination={
        'ToAddresses': ['test1@gmail.com', 'test2@gmail.com],
    },
    Message={
        'Body': {
            'Text': {
                'Charset': 'UTF-8',
                'Data': 'email body string',
            },
        },
        'Subject': {
            'Charset': 'UTF-8',
            'Data': 'email subject string',
        },
    },
    Source='sender.sendertest1@gmail.com',
)
