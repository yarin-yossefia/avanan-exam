import boto3,botocore 
#from errors import *
import s3transfer

#def Download_file(id,key,file):
def Download_file(file):
    s3 = boto3.resource(
        service_name='s3',
        region_name='us-east-2',
        aws_access_key_id='AKIAYCLGEJNDWM6R4LVK',
        aws_secret_access_key='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'

    )
    # select bucket
    my_bucket = s3.Bucket('exam-checkpoint-yarin')
    # download file into current directory
    for s3_object in my_bucket.objects.all():
        filename = s3_object.key
        if file in filename:
            full_path = filename
    
    s3.Bucket('exam-checkpoint-yarin').download_file(full_path, file)
    print("{} downloaded".format(full_path))
#Download_file('hello.txt')
