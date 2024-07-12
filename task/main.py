#http://devops-sample-bucket-boto3.s3-website.ap-south-1.amazonaws.com
import re
from scrape import website
from utils import listBuckets, deleteBucket,emptyBucket
from s3 import staticHost

def task():
    webName = input("Enter the Website Name: ")
    # proper website -> https:// name . nn
    pattern = r"^https:\/\/[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+\.(com|in|org|link)(\/.*)?$"
    check = re.match(pattern, webName)
    print(check)
    if check:
        bucketName = "devops-s3-dynamic-hosting-bucket"
        indexName = "app.html"
        url = "index.html"
        region = "ap-south-1"
        website(webName, url)
        availableBuck = listBuckets()
        isAvailable = False
        for data in availableBuck:
            if data["Name"] == bucketName:
                isAvailable = True
                break
            else:
                isAvailable = False
        
        if isAvailable:
            emptyBucket(bucketName)
            deleteBucket(bucketName)
            staticHost(BucketName=bucketName, indexName=indexName, url=url, region=region)
        else:
            staticHost(BucketName=bucketName, indexName=indexName, url=url, region=region)
        print(f"your website link is http://{bucketName}.s3-website.{region}.amazonaws.com")
    else:
        print("Enter a valid URL")
    return

task()