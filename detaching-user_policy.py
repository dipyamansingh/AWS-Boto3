import boto3
iam = boto3.client('iam')

iam.detach_user_policy(
 UserName = 'John', 
 PolicyArn='arn:aws:iam::aws:policy/AmazonEC2FullAccess'
)
