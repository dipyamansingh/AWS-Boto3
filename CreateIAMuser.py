import boto3
iam = boto3.client('iam')
response = iam.create_user(
    UserName='Dipyaman_211'
)

print(response)
