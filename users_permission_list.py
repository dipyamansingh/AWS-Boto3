import boto3
iam = boto3.client('iam')

for user_detail in iam.get_account_authorization_details(Filter=['User'])['UserDetailList']:
 policyname = []
 policyarn = []
 
 for policy in user_detail['AttachedManagedPolicies']:
 policyname.append(policy['PolicyName'])
 policyarn.append(policy['PolicyArn'])
 
 print("User: {0}\nUserID: {1}\nPolicyName: {2}\nPolicyARN: {3}\n".format(
 user_detail['UserName'],
 user_detail['UserId'],
 policyname,
 policyarn
 )
 )
