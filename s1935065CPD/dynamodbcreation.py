import boto3
from dotenv import load_dotenv
import os
import time

load_dotenv()
access_key = os.environ.get('aws_access_key_id')
secret_key = os.environ.get('aws_secret_access_key')
session_key = os.environ.get('aws_session_token')

# Create DynamoDB client
dynamodb = boto3.client('dynamodb',
                       aws_access_key_id=access_key,
                        aws_secret_access_key=secret_key,
                        region_name='us-east-1',
                        aws_session_token=session_key)

# Create CloudFormation client
cloudformation = boto3.client('cloudformation',
                        aws_access_key_id=access_key,
                        aws_secret_access_key=secret_key,
                        region_name='us-east-1',
                        aws_session_token=session_key)

with open('dynamictable.json', 'r') as f:
    template_body = f.read()

stack_name = 'myajaodynamodbs1935065table'

response = cloudformation.create_stack(
    StackName=stack_name,
     TemplateBody=template_body,
    Parameters=[
        {
            'ParameterKey': 'HashKeyElementName',
            'ParameterValue': 'imagename'
        },
        {
            'ParameterKey': 'StreamViewType',
            'ParameterValue': 'NEW_AND_OLD_IMAGES'
        }
    ]
)
print('Created CloudFormation stack with ID:', response['StackId']) 