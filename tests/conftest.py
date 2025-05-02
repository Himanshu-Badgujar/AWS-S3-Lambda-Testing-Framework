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

