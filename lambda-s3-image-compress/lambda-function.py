from __future__ import print_function

import json, os
import urllib
import boto3

print('Loading function')

s3 = boto3.client('s3')


def compress(body, key):
    import zipfile, StringIO
    data = StringIO.StringIO()
    with zipfile.ZipFile(data, 'w', zipfile.ZIP_DEFLATED) as f:
        f.writestr(os.path.basename(key), body)
    data.seek(0)
    return data.read()


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'].decode('utf8'))

    new_key = "compressed/%s.zip" % os.path.basename(key)

    body = s3.get_object(Bucket=bucket, Key=key)['Body'].read()

    s3.put_object(
        Body=compress(body,key),
        Key=new_key,
        Bucket=bucket,
    )

    return "OK"