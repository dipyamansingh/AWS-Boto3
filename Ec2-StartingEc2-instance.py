import boto3
ec2 = boto3.resource('ec2')
ec2.Instance('i-02a9d7a2cad784e74').start()
