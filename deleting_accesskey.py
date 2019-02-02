mport boto3
iam = boto3.client('iam')
iam.delete_access_key(
    AccessKeyId='AKIAJOFVR74W3FM6O2RA',
    UserName='Dipyaman_211'
