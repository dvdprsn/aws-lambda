import json
import boto3 
import base64
s3 = boto3.client('s3')
def lambda_handler(event, context):
    try:
        bucket = event['queryStringParameters']['Bucket']
        filename = event['queryStringParameters']['filename']
    except Exception as e:
        return {
            'statusCode': 404,
            'body': 'Failed to locate Bucket and filename in http request (try: [API url]?Bucket=[bucketname]&filename=[filepath])'
        }
    
    try:
        response = s3.get_object(Bucket=bucket, Key=filename)
        file = response['Body'].read()
        ret = base64.b64encode(file)
    except Exception as e:
        return {
            'statusCode': 404,
            'body': json.dumps('Error downloading file from S3: {}'.format(str(e)))
        }
        
    return {
        'statusCode': 200,
        'body': ret,
        'isBase64Encoded': True,
        'headers': {
            'Content-Type': response['ContentType'],
            'Content-Disposition': 'attachment; filename=' + filename
        }
    }
