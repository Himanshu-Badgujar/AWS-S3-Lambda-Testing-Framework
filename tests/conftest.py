import pytest
import boto3
import uuid
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def aws_region():
    return os.getenv("AWS_DEFAULT_REGION", "eu-north-1")

@pytest.fixture(scope="session")
def bucket_name():
    return os.getenv("BUCKET_NAME")

@pytest.fixture(scope="session")
def s3_client():
    return boto3.client("s3")

@pytest.fixture(scope="session")
def logs_client(aws_region):
    return boto3.client("logs", region_name=aws_region)

@pytest.fixture
def test_image_key():
    return f"test-upload-{uuid.uuid4().hex[:8]}.png"

@pytest.fixture
def upload_test_image(s3_client, bucket_name, test_image_key):
    with open("test_image.png", "rb") as f:
        s3_client.upload_fileobj(f, bucket_name, test_image_key)

    yield test_image_key

    print(f"Cleaning up: deleting {test_image_key}")
    s3_client.delete_object(Bucket=bucket_name, Key=test_image_key)

