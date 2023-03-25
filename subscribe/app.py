import json
import boto3

s3 = boto3.client("s3")


def change_log(new_line, bucket):

    # Get log file
    # update log file
    # put log file
    try:
        resp = s3.get_object(Bucket=bucket, Key='log.txt')
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': 'Error: Failed to locate log.txt in source bucket'
        }
    content = resp['Body'].read().decode('utf-8')
    new_content = content + new_line
    try:
        s3.put_object(Bucket=bucket, Key='log.txt', Body=str(new_content))
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': 'Error: Failed to update log.txt in source bucket'
        }


def get_subs(bucket):
    # get json list of subscribers
    try:
        resp = s3.get_object(Bucket=bucket, Key='sub_list.json')
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': 'Error: Failed to locate sub_list.json in source bucket'
        }

    file = resp['Body'].read()
    s3_string = file.decode('utf-8')

    json_obj = json.loads(s3_string)
    return json_obj


def handler(event, context):

    # Get the new file put on S3
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    src = {'Bucket': bucket, 'Key': key}

    # For each -> put new file into their bucket
    subs = get_subs(bucket)
    change_log('New file uploaded and sent to subscribers: ' + key + '\n', bucket)
    for item in subs:
        try:
            s3.copy_object(CopySource=src, Bucket=subs[item], Key=key)
        except Exception as e:
            print(e)
            return {
                'statusCode': 500,
                'body': 'Error: Failed to copy object to destination bucket'
            }

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
