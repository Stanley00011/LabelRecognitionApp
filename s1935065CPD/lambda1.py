import json
import boto3

s3_client = boto3.client('s3')
rekognition_client = boto3.client('rekognition')
dynamodb_client = boto3.client('dynamodb')

def lambda_handler(event, context):
    bucket_name = 'mybuckets1935065'  
    response = s3_client.list_objects_v2(Bucket=bucket_name)

    for obj in response['Contents']:
        object_key = obj['Key']
        image_name = object_key.split('/')[-1]

        # Retrieve the object from S3 and get image bytes from the response
        response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
        image_bytes = response['Body'].read()

        # Detect labels in the image using Rekognition
        response = rekognition_client.detect_labels(Image={'Bytes': image_bytes}, MaxLabels=10, MinConfidence=50)
        labels = [{'Name': label['Name'], 'Confidence': label['Confidence']} for label in response['Labels']]

        # Get the top five labels with their confidence scores
        top_five_labels = sorted(labels, key=lambda x: x['Confidence'], reverse=True)[:5]

        # Print the image name, image bytes, and detected labels with confidence levels
        print(f'Image name: {image_name}')
        print(f'Image bytes: {image_bytes}')
        print('Top five labels with confidence levels:')
        for label in top_five_labels:
            print(f'Label: {label["Name"]}, Confidence: {label["Confidence"]}')

        # Store the top five detected labels in a DynamoDB table
        item = {
            'imagename': {'S': image_name},
            'labels': {'L': [{'M': {'name': {'S': label['Name']}, 'confidence': {'N': str(label['Confidence'])}}} for label in top_five_labels]}
        }
        dynamodb_client.put_item(TableName='myajaodynamodbs1935065table', Item=item)

        # Check if 'pedestrian' is one of the top five labels
        if any(label['Name'] == 'Pedestrian' for label in top_five_labels):
            print('Pedestrian detected!')

    return {
        'statusCode': 200,
        'body': json.dumps('Successfully processed all images')
    }
