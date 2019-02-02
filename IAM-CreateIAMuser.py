import boto3
iam = boto3.client('iam')
response = iam.create_user(
    UserName='dipyaman_211'
)

print(response)

