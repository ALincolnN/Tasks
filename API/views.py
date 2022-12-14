from .models  import Task
from django.shortcuts import render,redirect
from django.http import JsonResponse

from rest_framework.decorators import api_view
#from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response

from .serializers import TaskSerializer


# Create your views here.


@api_view(['GET'])
def apiGuide(request):
    api_urls = {
        'list': '/task-list/',
        'Detail-View' : '/task-detail/<str:pk>/',
        'Create' : '/task-create/',
        'Update' : '/task-update/<str:pk>/',
        'Delete' : '/task-delete/<str:pk>'
    }
    return Response(api_urls)


@api_view(['GET'])
def tasklist(request):

    tasks=Task.objects.all().order_by('-id')
    serializer=TaskSerializer(tasks,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request,pk):

    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many = False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):

    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request,pk):
    task = Task.objects.get(id=pk)

    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
#@csrf_exempt
def taskDelete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return redirect('/')

   

    
   