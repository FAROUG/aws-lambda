import boto3
import os
from smart_open import smart_open

s3 = boto3.client('s3')
response = s3.list_buckets()
# allowing the user to search by any word without worrying about the case sensitivity of the search word
string1 = bytes(os.environ['string'], 'utf-8').lower()


# Python 3 code to demonstrate
# the removal of all occurrences of
# a given item using filter() and __ne__

def remove_items(test_list, item):
    # using filter() + __ne__ to perform the task
    res = list(filter((item).__ne__, test_list))

    return res


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
                words = []
                line_index += 1
                word_index = 0
                line = line.decode('utf8').split(' ')
                line_after_removed = remove_items(line, '')
                for word in line_after_removed:
                    word = bytes(word.lower(), 'utf-8', errors="strict")
                    words.append(word)
                    word_index += 1
                    if string1 in word:
                        print('String', string1, 'The word number is approximately', word_index, 'Found In Line',
                              line_index, 'in file name', object_name, 'bucket ', bucket_name)


def lambda_handler(event, context):

    bucket_name = os.environ['bucket_name']
    print(bucket_name)
    # bucket_name = 'weekly.email'  # hard coded value to test
    list_of_buckets_name = []
    for buckets in response['Buckets']:
        list_of_buckets_name.append(buckets['Name'])
    if bucket_name == "":
        print("Search will start on all S3 buckets")
        for bucket_name in list_of_buckets_name:
            print("Search started on bucket", bucket_name)
            getting_object(bucket_name)
    elif bucket_name not in list_of_buckets_name:
        print(
            f"Please Make sure that this entered bucket name is correct {bucket_name} "
            f"or you have the correct access ")
        print(f'List of existing buckets:{list_of_buckets_name}')
    else:
        print(f"The bucket exist {bucket_name}")
        getting_object(bucket_name)
