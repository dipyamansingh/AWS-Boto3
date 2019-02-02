import boto3
iam = boto3.client('iam')


iam.create_user( UserName='Deeep')

iam.attach_user_policy(
 UserName = 'Deep', 
 PolicyArn='arn:aws:iam::aws:policy/AmazonEC2FullAccess'
)
