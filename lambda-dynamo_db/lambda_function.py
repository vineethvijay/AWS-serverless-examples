import time
from datetime import datetime
import boto3

DDB= boto3.resource('dynamodb').Table('logtime')

def lambda_handler(event, context):
    now = datetime.utcnow()
    timestamp = int(time.mktime(now.timetuple()))

    item = {
        'Item': {
            'timestamp': timestamp,
            'datetime' : now.isoformat(),
            'message' : "Written to table"
        }

    }
    print("Item: %s" % item)

    DDB.put_item(**item)

    return item
