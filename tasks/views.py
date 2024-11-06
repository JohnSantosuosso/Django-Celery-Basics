from django.http import JsonResponse
from .tasks import long_running_task, process_data

def trigger_task(request):
    """
    View to trigger a long-running task
    """
    task = long_running_task.delay(10)
    return JsonResponse({
        "message": "Task started",
        "task_id": task.id
    })

def process_text(request):
    """
    View to process text data
    """
    text = request.GET.get('text', 'default text')
    task = process_data.delay(text)
    return JsonResponse({
        "message": "Processing started",
        "task_id": task.id
    })