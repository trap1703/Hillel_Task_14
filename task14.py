
# task 14
import boto3
import argparse
import sys

#==========================================
parser = argparse.ArgumentParser()
parser.add_argument(
    '--name',
    type=str,
    default="Name",
    help='min an integer (default: 10)'
)
parser.add_argument(
    '--min',
    type=int,
    default=10,
    help='min an integer (default: 10)'
)
parser.add_argument(
    '--max',
    type=int,
    default=10,
    help='max an integer (default: 10)'
)
parser.add_argument(
    '--descap',
    type=int,
    default=10,
    help='descap an integer (default: 10)'
)
args = parser.parse_args()
#print(f'Hello {args.name}')
nameasg = args.name
min = args.min
max = args.max
descap = args.descap
#print ("Nane ASG   : ", nameasg)
#print ("MIN ASG   : ", min)
#print ("MAX ASG   : ", max)
#print ("Descap ASG   : ", descap)
if min != 10:
    print ("run programm")
    client = boto3.client('autoscaling')
    group = client.describe_auto_scaling_groups(AutoScalingGroupNames=[nameasg])['AutoScalingGroups'][0]
    new = client.update_auto_scaling_group(AutoScalingGroupName=nameasg, DesiredCapacity=descap)
    new = client.update_auto_scaling_group(AutoScalingGroupName=nameasg, MinSize=min)
    new = client.update_auto_scaling_group(AutoScalingGroupName=nameasg, MaxSize=max)
    print ("Apply new parametrs min,max and descap parametrs")
    print ("New parametrs for ASG : ", nameasg)
    print ("Max size group  : ", max)
    print("Min size group  : ", min)
    print("descap size group  : ", descap)
if min == 10:
    print ("Not input min and max parametrs")
    print ("Curent parametrs for ASG : ", nameasg)
    client = boto3.client('autoscaling')
    group = client.describe_auto_scaling_groups(AutoScalingGroupNames=[nameasg])['AutoScalingGroups'][0]
    print ("Max size group  : ", group['MaxSize'])
    print("Min size group  : ", group['MinSize'])
    print("descap size group  : ", group['DesiredCapacity'])
#print (max)



