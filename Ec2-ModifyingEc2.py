import boto3
ec2 = boto3.client('ec2')


instance_id = 'i-02a9d7a2cad784e74'

ec2.stop_instances(InstanceIds=[instance_id])
waiter=ec2.get_waiter('instance_stopped')
waiter.wait(InstanceIds=[instance_id])

ec2.modify_instance_attribute(InstanceId=instance_id, Attribute='instanceType', Value='t2.small')

ec2.start_instances(InstanceIds=[instance_id])
