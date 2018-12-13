def lambda_handler(event, context):
    name=event.get('name')
    return {
        'message:' : name
    }

