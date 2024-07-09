import boto3
s3 = boto3.client("s3")

def createBucket():
    s3 = boto3.client("s3").create_bucket(
         Bucket='devops-sample-bucket-boto3',
         CreateBucketConfiguration= {
             'LocationConstraint': 'ap-south-1'
         }
    )
    print(s3)
    return

# createBucket()

def putBucketAcl():
    response = s3.put_public_access_block(
        Bucket = "devops-sample-bucket-boto3",
        PublicAccessBlockConfiguration={
        'BlockPublicAcls': False,
        'IgnorePublicAcls': False,
        'BlockPublicPolicy': False,
        'RestrictPublicBuckets': False
    },
    )
    print(response)
    return

# putBucketAcl()


def bucketOwnership():
    response = s3.put_bucket_ownership_controls(
    Bucket="devops-sample-bucket-boto3",
    OwnershipControls={
        'Rules': [
            {
                'ObjectOwnership': 'BucketOwnerPreferred'
            },
        ]
    }
    )
    print(response)
    return

# bucketOwnership()

def putObject():
    with open("index.html", "rb") as data:
        value = s3.put_object(
            ACL = 'public-read',
            Bucket = 'devops-sample-bucket-boto3',
            Body = data,
            Key = "app.html",
            ContentType = "text/html"
        )
        
    print(value)
    return

putObject()

def staticWebsiteHost():
    response = s3.put_bucket_website(
    Bucket='devops-sample-bucket-boto3',
    WebsiteConfiguration={
        'IndexDocument': {
            'Suffix': 'app.html'
        }
    }
)
    print(response)
    return

# staticWebsiteHost()


def putObjectAcl():
    response = s3.put_object_acl(
        ACL='public-read',
        Bucket='devops-sample-bucket-boto3',
        Key = "app.html"
    )
    print(response)
    return

# putObjectAcl()