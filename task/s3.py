from utils import createBucket, putBucketAcl, bucketOwnership, putObject, staticWebsiteHost

def staticHost(BucketName, indexName, url, region):
    createBucket(BucketName, region)
    putBucketAcl(BucketName)
    bucketOwnership(BucketName)
    putObject(BucketName=BucketName, indexName= indexName, objectUrl=url)
    staticWebsiteHost(BucketName=BucketName, indexName=indexName)
    return