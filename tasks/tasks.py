from celery import shared_task
import time

@shared_task
def long_running_task(duration):
    """
    A sample long-running task that simulates work by sleeping
    """
    time.sleep(duration)
    return f"Task completed after {duration} seconds"

@shared_task
def process_data(data):
    """
    A sample task that processes data
    """
    # Simulate processing
    time.sleep(2)
    result = f"Processed data: {data.upper()}"
    return result