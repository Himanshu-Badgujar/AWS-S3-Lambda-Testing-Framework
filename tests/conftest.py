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

@pytest.fixture(scope="session", autouse=True)
def global_teardown():
    print("\n[Setup] Starting test session...")
    yield
    print("\n[Teardown] Test session completed. Performing global cleanup...")

    bucket_name = os.getenv("BUCKET_NAME")
    region = os.getenv("AWS_DEFAULT_REGION", "eu-north-1")
    s3 = boto3.client("s3", region_name=region)

    response = s3.list_objects_v2(Bucket=bucket_name, Prefix="test-upload-")
    if "Contents" in response:
        for obj in response["Contents"]:
            print(f"Cleaning up: deleting {obj['Key']}")
            s3.delete_object(Bucket=bucket_name, Key=obj["Key"])
    else:
        print("No test-upload files found for cleanup.")

    print("[Teardown] Global cleanup complete.")