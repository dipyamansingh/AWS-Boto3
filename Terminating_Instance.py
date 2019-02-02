import boto3
ec2 = boto3.resource('ec2')
instance_id = 'i-02a9d7a2cad784e74'
instance = ec2.Instance(instance_id)
response = instance.terminate()
print(response)
