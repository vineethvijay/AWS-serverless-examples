from __future__ import print_function

import json
import boto3

client = boto3.client("sns")

print('Loading function')

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    message = event['Records'][0]['Sns']['Message']
    print("Unfiltered message: " + message)
    message+="-filtered"

    client.publish(Message=message, TopicArn="arn:aws:sns:eu-west-1:801771690413:topic2")
    return "ok"
