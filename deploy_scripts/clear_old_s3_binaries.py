import os
os.popen("pip install -U boto3")
import boto3

bucket_name = "circleci-unique-bucket"
ACCESS_KEY = "your-key-here"
SECRET_KEY = "your-secret"

client = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
)

try:
    for revision in client.list_objects(Bucket=bucket_name)["Contents"]:
        client.delete_object(Bucket=bucket_name, Key=revision["Key"])
except:
    pass # if not files exist that is still OK
