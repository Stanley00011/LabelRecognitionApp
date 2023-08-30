import boto3
from dotenv import load_dotenv
import os
import time

load_dotenv()
access_key = os.environ.get('aws_access_key_id')
secret_key = os.environ.get('aws_secret_access_key')
session_token = os.environ.get('aws_session_token')

sns_client = boto3.client('sns',
                        aws_access_key_id=access_key,
                        aws_secret_access_key=secret_key,
                        region_name='us-east-1',
                        aws_session_token=session_token)

response = sns_client.create_topic(
    Name='mys1935065sns'
)

topic_arn = response['TopicArn']

print(f'SNS Topic ARN: {topic_arn}')

response = sns_client.subscribe(
    TopicArn=topic_arn,
    Protocol='email',
    Endpoint='o.ajao@alustudent.com'
)

subscription_arn = response['SubscriptionArn']

print(f'SNS Subscription ARN: {subscription_arn}')
