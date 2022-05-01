from dotenv import load_dotenv
from botocore.exceptions import ClientError
import boto3
import os


load_dotenv()
AWS_STORAGE_BUCKET_NAME = "wehelp-third-phase-week1"

s3_client = boto3.client("s3", aws_access_key_id= os.getenv("AWS_ACCESS_KEY_ID"), aws_secret_access_key= os.getenv("AWS_SECRET_KEY"))

def upload_file_to_s3(file, bucket, file_name):

  try:
    s3_client.upload_fileobj(file, bucket,f"img/{file_name}", ExtraArgs={'ContentType': "image/jpeg"})
    return True
  except ClientError as e:

    print(e)
    return False



# upload_file_to_s3("../static/img/111.jpg", "wehelp-third-phase-week1")
# response = s3_client.list_buckets()


# def upload_file_to_s3(file, bucket_name, acl="public_read"):  #(object_name=None, args=None)
#   try:
#     s3_client.upload_fileobj(file, bucket_name, file.filename,
#     ExtraArgs={"ACL": acl, 'ContentType': file.content_type})
#   except Exception as e:


#   response = s3_client.upload_file(file_name, bucket, object_name)


  # response = client.upload_file(file_name, bucket, object_name, ExtraArgs=args)





