from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task


class TaskView(APIView):
    def get(self, request, id=None):
        if id:
            try:
                task = Task.objects.get(id=id)
            except Task.DoesNotExist:
                return Response({"message": "No task found"})
            if task:
                serializer = TaskSerializer(task)
                return Response(serializer.data)
        else:
            tasks = Task.objects.all()
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def put(self, request):
        try:
            task = Task.objects.get(id=request.data["id"])
        except Task.DoesNotExist:
            return Response({"message": "No task found"})
        if task:
            serializer = TaskSerializer(instance=task, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response({"message": "Invalid data"})

    def delete(self, request, id=None):
        try:
            task = Task.objects.get(id=id)
        except Task.DoesNotExist:
            return Response({"message": "No task found"})
        if task:
            task.delete()
            return Response({"message": "Task deleted"})
        return Response({"message": "Invalid data"})
