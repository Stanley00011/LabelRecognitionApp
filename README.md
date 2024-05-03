AWS Label Detection and Notification System

Overview
This project implements an AWS-based Label Detection and Notification System designed to detect labels in images uploaded to an S3 bucket and trigger email alerts for specific labels using AWS services like EC2, S3, SQS, Lambda, DynamoDB, and SNS. The system is built to seamlessly handle image uploads, label identification, and notification processes.

Components
1. EC2 Instance
An EC2 instance is utilized to host the Python application responsible for uploading images to the S3 bucket.

2. S3 Bucket
The S3 bucket serves as the storage repository for the images uploaded by the EC2 instance.

3. SQS (Simple Queue Service)
SQS is used to manage the message queue, facilitating communication between the EC2 instance and Lambda function.

4. Lambda Function
AWS Lambda is employed to execute code in response to events, such as image uploads. The Lambda function interacts with S3, DynamoDB, and AWS Rekognition for label detection.

5. DynamoDB
DynamoDB is utilized as a NoSQL database to store metadata and information related to processed images and detected labels.

6. AWS Rekognition
AWS Rekognition is a deep learning-based image analysis service used for label detection in uploaded images.

7. SNS (Simple Notification Service)
SNS is employed to send email alerts for the detection of specific labels in images.

Workflow
The Python application running on the EC2 instance uploads images to the designated S3 bucket using Boto3, AWS SDK for Python.
Upon successful upload, S3 triggers an event notification that is sent to SQS.
The Lambda function is configured to listen to messages from the SQS queue. Once a message is received, Lambda retrieves the image from S3 and invokes AWS Rekognition for label detection.
Detected labels are stored in DynamoDB along with relevant metadata.
If specific labels are detected, SNS is triggered to send email alerts to the configured recipients.

Setup and Configuration
AWS Account: Ensure you have an AWS account with appropriate permissions to create and manage EC2 instances, S3 buckets, SQS queues, Lambda functions, DynamoDB tables, SNS topics, and IAM roles.
IAM Roles: Set up IAM roles with necessary permissions for EC2, Lambda, and other AWS services involved.
Configuration Files: Update configuration files with AWS credentials, S3 bucket names, SQS queue URLs, and other relevant information.
Deploy: Deploy the Python application to the EC2 instance and configure Lambda function.

Usage
Upload images to the designated S3 bucket.
Monitor the email alerts for label detections based on configured triggers.

Dependencies
Boto3: AWS SDK for Python
AWS CLI: Command-line tool for interacting with AWS services
