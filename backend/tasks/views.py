from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Task
# Create your views here.

def task_list(request):
    data = Task.objects.all()
    tasks = [t.to_json() for t in data]
    return JsonResponse(tasks, safe=False)

@csrf_exempt
def create_task(request):
    print(request.POST)
    if request.method == "POST":
        title = request.POST.get('title')
        project = request.POST.get('project')
        date = request.POST.get('date')

        real_date = datetime.fromisoformat(str(date))

        task = Task.objects.create(title=title, project=project, date=real_date)
        return JsonResponse({'id': task.id})
    else:
        print('Trouxa!!!!')