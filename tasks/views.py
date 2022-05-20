from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from tasks.models import Task

def task_list(request):
    tasks = [{'id': task.id,
              'title': task.title,
              'completed': task.completed} for task in Task.objects.all()]
    return JsonResponse(status=200, data=tasks, safe=False)

@csrf_exempt
def create_task(request):
    title = request.POST.get('title')
    print(request.POST)
    if not title:
        task = Task.objects.create(title="mY FIRST TITLE")
        return JsonResponse(status=400, data={'error': 'title is required'})
    task = Task.objects.create(title=title)
    return JsonResponse(status=201, data={'title': task.title,
                                          'completed': task.completed,

                                          'id': task.id}, safe=False)

@csrf_exempt
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return JsonResponse(status=204, data={'message': 'task deleted'})

@csrf_exempt
def update_task_status(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    status = request.POST.get('status')
    if not status:
        return JsonResponse(status=400, data={'error': 'status is required'})
    task.completed = int(status)
    task.save()
    return JsonResponse(status=204, data={'message': 'task status updated'})

def index(request):
    return render(request, 'tasks/addtask.html')

