from django.shortcuts import render
from django.http import JsonResponse
from .models import Task

# Create your views here.

def task_list(request):
    data = Task.objects.all()
    tasks = [t.to_json() for t in data]
    return JsonResponse(tasks, safe=False)