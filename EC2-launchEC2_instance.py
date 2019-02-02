import boto3

ec2 = boto3.client('ec2')
instance = ec2.run_instances(ImageId='ami-0ff8a91507f77f867',MinCount=1,MaxCount=1)
