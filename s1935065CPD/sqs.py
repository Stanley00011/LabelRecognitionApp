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


sqs = boto3.resource('sqs', 
                        aws_access_key_id=access_key,
                        aws_secret_access_key=secret_key,
                        region_name='us-east-1',
                        aws_session_token=session_key)
queue = sqs.create_queue(QueueName='myqueues1935065', Attributes={'DelaySeconds': '5'})

print(queue.url)
print(queue.attributes.get('DelaySeconds'))