import boto3

iam = boto3.client('iam')

response = iam.create_access_key(
    UserName='Dipyaman_211'
)

print(response['AccessKey'])
