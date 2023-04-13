from main import delivery


def lambda_handler(event, context):
    delivery()

    return {
        'statusCode': 200
    }

