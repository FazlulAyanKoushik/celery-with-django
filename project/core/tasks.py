import json

from celery import shared_task
from django_celery_beat.models import IntervalSchedule, PeriodicTask


@shared_task(bind=True)
def test_func(self):
    # Operations
    for i in range(10):
        print(i)
    return "Done"


@shared_task(name="clear_session_cache")
def clear_session_cache(id):
    print(f"Session Cache Cleared: {id}")
    return id


@shared_task(name="clear_redis_data")
def clear_redis_data(key):
    print(f"Redis Data Cleared: {key}")
    return key


@shared_task
def clear_rabbitmq_data(key):
    print(f"RabbitMQ Data Cleared: {key}")
    return key


# ===========================
# Method 4
# ==========================
# Create Schedule every 30 seconds
schedule, created = IntervalSchedule.objects.get_or_create(
    every=30,
    period=IntervalSchedule.SECONDS,
)
# Schedule the periodic task programmatically
PeriodicTask.objects.get_or_create(
    name='Clear RabbitMQ Periodic Task',
    task='myapp.tasks.clear_rabbitmq_data',
    interval=schedule,
    args=json.dumps(['hello']),  # Pass the arguments to the task as a JSON-encoded list
)
