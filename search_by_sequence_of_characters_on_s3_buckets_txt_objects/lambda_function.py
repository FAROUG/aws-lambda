import boto3
import os
from re import search
from smart_open import smart_open

s3 = boto3.client('s3')
response = s3.list_buckets()
# allowing the user to search by any word without worrying about the case sensitivity of the search word
sentence = (bytes(os.environ['sentence'], 'utf-8').lower()).decode("utf-8") 


def getting_object(bucket_name):
    objects = s3.list_objects_v2(Bucket=bucket_name)
    objects_contents = objects['Contents']
    for each_object_content in objects_contents:
        object_name = each_object_content['Key']
        obj = s3.get_object(Bucket=bucket_name, Key=object_name)
        obj_type = obj['ContentType']
        if obj_type == "text/plain":
            line_index = 0
            for line in smart_open(f's3://{bucket_name}/{object_name}', 'rb'):
                line = line.decode("utf-8").lower()
                line_index += 1
                if sentence == "":
                    print("please enter a word or a sentence")
                    return            
                if search(sentence, line):
                    print('Sentence', sentence, 'this sentence found in line',
                            line_index, 'in file name', object_name, 'bucket ', bucket_name)  


def lambda_handler(event, context):

    bucket_name = (os.environ['bucket_name']).lower()
    print(bucket_name)
    # bucket_name = 'weekly.email'  # hard coded value to test
    list_of_buckets_name = []
    for buckets in response['Buckets']:
        list_of_buckets_name.append(buckets['Name'])
    if bucket_name == "":
        print("The search will start on all S3 buckets")
        for bucket_name in list_of_buckets_name:
            print("The search started on bucket", bucket_name)
            getting_object(bucket_name)
    elif bucket_name not in list_of_buckets_name:
        print(
            f"Please Make sure that this entered bucket name {bucket_name} is correct "
            f"or you have the correct access ")
        print(f'List of existing buckets:{list_of_buckets_name}')
    else:
        print(f"The bucket exist {bucket_name}")
        getting_object(bucket_name)
