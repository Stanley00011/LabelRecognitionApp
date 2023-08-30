import boto3
from dotenv import load_dotenv
import os
import json
import logging
import glob
import time
from botocore.exceptions import ClientError



# Let's use Amazon S3
load_dotenv()
access_key = os.environ.get('aws_access_key_id')
secret_key = os.environ.get('aws_secret_access_key')
session_key = os.environ.get('aws_session_token')


ec2 = boto3.resource('ec2', aws_access_key_id=access_key,
                        aws_secret_access_key=secret_key,
                        region_name='us-east-1',
                        aws_session_token=session_key)

instances = ec2.create_instances(
        ImageId="ami-005f9685cb30f234b",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="vockey"
    )