import boto3

cloudwatch = boto3.client('cloudwatch')

cloudwatch.delete_alarms(
  AlarmNames=['Web_Server_CPU_Utilization'],
)
