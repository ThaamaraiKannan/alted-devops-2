import boto3

def createKey():
    ec2 = boto3.client("ec2", region_name = "ap-south-1")
    value = ec2.create_key_pair(
        KeyName = "devops1",
        KeyType = "rsa",
        KeyFormat = "pem"
    )
    print(value)
    with open("devops1.pem", "w") as f:
        f.write(value["KeyMaterial"])
    return

createKey()