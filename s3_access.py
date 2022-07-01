import boto3

access_id = "AKIAYOQUX76QUACWQIML"
secret = "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"
region = "ap-south-1"

session = boto3.Session(aws_access_key_id=access_id, aws_secret_access_key=secret, region_name=region)
s3 = session.resource("s3")

for bucket in s3.buckets.all():
    print(bucket.name)
    for file in bucket.objects.all():
        print(file.key)

s3_client = boto3.client('s3', aws_access_key_id=access_id, aws_secret_access_key=secret, region_name=region)
