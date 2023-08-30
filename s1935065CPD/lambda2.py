import json
import boto3

sns_client = boto3.client('sns')

def lambda_handler(event, context):
    for record in event['Records']:
        if record['eventName'] == 'INSERT':
            # Extract the image name and labels from the DynamoDB record
            new_image = record['dynamodb']['NewImage']
            image_name = new_image['imagename']['S']
            labels = new_image['labels']['L']

            # Check if 'pedestrian' is one of the labels
            for label in labels:
                if label['M']['name']['S'] == 'Pedestrian' and float(label['M']['confidence']['N']) >= 90:
                    pedestrian_confidence = label['M']['confidence']['N']
                    message = f"Pedestrian detected in image {image_name} with confidence level {pedestrian_confidence}"
                    response = sns_client.publish(TopicArn='arn:aws:sns:us-east-1:066987774992:mys1935065sns', Message=message)
                    print(f"SNS message sent: {response['MessageId']}")

    return {
        'statusCode': 200,
        'body': json.dumps('Successfully processed all records')
    }
