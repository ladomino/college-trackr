from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.task import Task as TaskModel
from ..serializers import TaskSerializer

class TaskList(generics.ListCreateAPIView):
    
    #permission_classes=(IsAuthenticated,)
    serializer_class = TaskSerializer

    def get(self, request):
        tasks = TaskModel.objects.all()
        data = TaskSerializer(tasks, many=True).data
        return Response({ 'tasks': data })

    def post(self, request):
        # """Create request"""
        # Add user to request data object
        # request.data['college']['owner'] = request.user.id
        # # Serialize/create mango
        task = TaskSerializer(data=request.data['task'])
        # If the college data is valid according to our serializer...
        if task.is_valid():
            # Save the created college & send a response
            task.save()
            return Response({ 'task': task.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(task.errors, status=status.HTTP_400_BAD_REQUEST)