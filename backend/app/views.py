from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task

class TaskView(APIView):
    
    def get(self, request):
        try:
            tasks = [task for task in Task.objects.all().order_by('created')]
        except Task.DoesNotExist:
            return Response({'message': 'No tasks found'})
        if tasks:
            serializer = TaskSerializer(tasks, many=True)
            if serializer.is_valid():
                return Response(serializer.data)
            return Response({'message': 'Invalid data'})
    
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def put(self, request):
        try:
            task = Task.objects.get(id=request.data['id'])
        except Task.DoesNotExist:
            return Response({'message': 'No task found'})
        if task:
            serializer = TaskSerializer(instance=task, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response({'message': 'Invalid data'})
    
    def delete(self, request):
        try:
            task = Task.objects.get(id=request.data['id'])
        except Task.DoesNotExist:
            return Response({'message': 'No task found'})
        if task:
            task.delete()
            return Response({'message': 'Task deleted'})
     
        