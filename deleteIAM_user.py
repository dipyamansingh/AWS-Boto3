import boto3
iam = boto3.client('iam')
iam.delete_user(
    UserName='Dipyaman_211'
)
