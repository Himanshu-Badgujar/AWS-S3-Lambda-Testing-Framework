import time

class LambdaTestBase:

    def __init__(self, logs_client, log_group):
        self.logs_client = logs_client
        self.log_group = log_group

    def get_recent_log_streams(self, limit=5):
        response = self.logs_client.describe_log_streams(
            logGroupName=self.log_group,
            orderBy="LastEventTime",
            descending=True,
            limit=limit
        )
        return [s["logStreamName"] for s in response.get("logStreams", [])]

    def get_log_events(self, stream_name):
        response = self.logs_client.get_log_events(
            logGroupName=self.log_group,
            logStreamName=stream_name,
            startFromHead=True
        )
        return [event["message"] for event in response["events"]]

    def wait_for_image_key_in_logs(self, image_key, retries=10, delay=5):
        """
        Waits until the uploaded image_key appears in any of the recent Lambda logs.
        """
        for attempt in range(retries):
            print(f"Attempt {attempt + 1}: checking logs for key '{image_key}'")
            for stream in self.get_recent_log_streams():
                logs = self.get_log_events(stream)
                if any(image_key in line for line in logs):
                    return True
            time.sleep(delay)
        return False
