from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView, DeleteView

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
        # # Serialize/create task
        task = TaskSerializer(data=request.data['task'])
        # If the college data is valid according to our serializer...
        if task.is_valid():
            # Save the created college & send a response
            task.save()
            return Response({ 'task': task.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(task.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the task to show
        task = get_object_or_404(TaskModel, pk=pk)
        # Only want to show owned tasks?
        # if request.user != task.owner:
        #     raise PermissionDenied('Unauthorized, you do not own this task')

        # Run the data through the serializer so it's formatted
        data = TaskSerializer(task).data
        return Response({ 'task': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate task to delete
        task = get_object_or_404(TaskModel, pk=pk)
        # Check the task's owner against the user making this request
        # if request.user != task.owner:
        #     raise PermissionDenied('Unauthorized, you do not own this task')
        # Only delete if the user owns the  task
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate Task
        # get_object_or_404 returns a object representation of our Task
        task = get_object_or_404(TaskModel, pk=pk)
        # Check the task's owner against the user making this request
        # if request.user != task.owner:
        #     raise PermissionDenied('Unauthorized, you do not own this task')

        # Ensure the owner field is set to the current user's ID
        # request.data['task']['owner'] = request.user.id
        # Validate updates with serializer
        data = TaskSerializer(task, data=request.data['task'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

  