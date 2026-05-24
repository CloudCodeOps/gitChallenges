import boto3

# ── Initialize EC2 client ────────────────────────────────────────
ec2 = boto3.client(
    "ec2",
    region_name="us-east-1",          # change to your region
    aws_access_key_id="YOUR_ACCESS_KEY",
    aws_secret_access_key="YOUR_SECRET_KEY",
    # Or use environment variables / IAM role (recommended)
)

# ── Create EC2 Instance ──────────────────────────────────────────
response = ec2.run_instances(
    ImageId="ami-0c02fb55956c7d316",   # Amazon Linux 2 (us-east-1)
    InstanceType="t2.micro",           # Free tier eligible
    MinCount=1,
    MaxCount=1,
    KeyName="your-key-pair-name",      # Must exist in AWS console
    SecurityGroupIds=["sg-xxxxxxxx"],  # Your security group ID
    SubnetId="subnet-xxxxxxxx",        # Your subnet ID
    TagSpecifications=[
        {
            "ResourceType": "instance",
            "Tags": [{"Key": "Name", "Value": "MyEC2Instance"}],
        }
    ],
    BlockDeviceMappings=[
        {
            "DeviceName": "/dev/xvda",
            "Ebs": {
                "VolumeSize": 20,       # GB
                "VolumeType": "gp3",
                "DeleteOnTermination": True,
            },
        }
    ],
    UserData="""#!/bin/bash
        yum update -y
        yum install -y httpd
        systemctl start httpd
        systemctl enable httpd
    """,
)

# ── Extract Instance Info ────────────────────────────────────────
instance = response["Instances"][0]
instance_id = instance["InstanceId"]
print(f"Instance created: {instance_id}")

# ── Wait until Instance is Running ──────────────────────────────
print("Waimport boto3

# ── Initialize EC2 client ────────────────────────────────────────
ec2 = boto3.client(
    "ec2",
    region_name="us-east-1",          # change to your region
    aws_access_key_id="YOUR_ACCESS_KEY",
    aws_secret_access_key="YOUR_SECRET_KEY",
    # Or use environment variables / IAM role (recommended)
)

# ── Create EC2 Instance ──────────────────────────────────────────
response = ec2.run_instances(
    ImageId="ami-0c02fb55956c7d316",   # Amazon Linux 2 (us-east-1)
    InstanceType="t2.micro",           # Free tier eligible
    MinCount=1,
    MaxCount=1,
    KeyName="your-key-pair-name",      # Must exist in AWS console
    SecurityGroupIds=["sg-xxxxxxxx"],  # Your security group ID
    SubnetId="subnet-xxxxxxxx",        # Your subnet ID
    TagSpecifications=[
        {
            "ResourceType": "instance",
            "Tags": [{"Key": "Name", "Value": "MyEC2Instance"}],
        }
    ],
    BlockDeviceMappings=[
        {
            "DeviceName": "/dev/xvda",
            "Ebs": {
                "VolumeSize": 20,       # GB
                "VolumeType": "gp3",
                "DeleteOnTermination": True,
            },
        }
    ],
    UserData="""#!/bin/bash
        yum update -y
        yum install -y httpd
        systemctl start httpd
        systemctl enable httpd
    """,
)

# ── Extract Instance Info ────────────────────────────────────────
instance = response["Instances"][0]
instance_id = instance["InstanceId"]
print(f"Instance created: {instance_id}")

# ── Wait until Instance is Running ──────────────────────────────
print("Wa
