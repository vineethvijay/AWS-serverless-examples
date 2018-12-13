import json

'''
#Configure Event in console

{
  "key1": "Hello",
  "key2": "world"
}

'''


def lambda_handler(event, context):
    message = '{} {}!'.format(event['key1'],
                              event['key2'])
    return {
        'message' : message
    }



