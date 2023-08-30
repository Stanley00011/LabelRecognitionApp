import boto3
from dotenv import load_dotenv
import os
import time

load_dotenv()
access_key = os.environ.get('aws_access_key_id')
secret_key = os.environ.get('aws_secret_access_key')
session_key = os.environ.get('aws_session_token')

s3 = boto3.client('s3', 
                        aws_access_key_id=access_key,
                        aws_secret_access_key=secret_key,
                        region_name='us-east-1',
                        aws_session_token=session_key)

sqs = boto3.client('sqs', 
                        aws_access_key_id=access_key,
                        aws_secret_access_key=secret_key,
                        region_name='us-east-1',
                        aws_session_token=session_key)

image_dir = 'images(1)'
bucket_name = 'mybuckets1935065'
upload_interval = 30
queue_url = 'https://sqs.us-east-1.amazonaws.com/066987774992/myqueues1935065'

for file in os.listdir(image_dir):
    if file.endswith('.jpg') or file.endswith('.png'):
        file_path = os.path.join(image_dir, file)
        with open(file_path, 'rb') as data:
            s3.upload_fileobj(data, bucket_name, file)
            print(f"Uploaded {file} to {bucket_name}")
        message = {
            'ContentType': 'text/plain',
            'Content': f"{file} has been uploaded to {bucket_name}"
        }
        sqs.send_message(QueueUrl=queue_url, MessageBody=str(message))
    time.sleep(upload_interval)
