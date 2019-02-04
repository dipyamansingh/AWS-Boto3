mport boto3

s3 = boto3.resource('s3')
s3.create_bucket(Bucket='mickubucket')

s3.create_bucket(Bucket='mickubucket', CreateBucketConfiguration={
    'LocationConstraint': 'us-east-1'})
