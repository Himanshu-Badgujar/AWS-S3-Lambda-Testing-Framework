from test_base.test_base import LambdaTestBase

def test_s3_upload_triggers_lambda(s3_client, bucket_name, logs_client, test_image_key):
    with open("test_image.png", "rb") as f:
        s3_client.upload_fileobj(f, bucket_name, test_image_key)

    log_group = "/aws/lambda/s3_image_trigger"
    base = LambdaTestBase(logs_client, log_group)

    found = base.wait_for_image_key_in_logs(test_image_key)
    assert found, f"Expected image key '{test_image_key}' not found in recent logs"
