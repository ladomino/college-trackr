from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView, DeleteView

from ..models.applicationtask import ApplicationTask as ApplicationTaskModel
from ..serializers import ApplicationTaskSerializer

class ApplicationTaskList(generics.ListCreateAPIView):
    
    permission_classes=(IsAuthenticated,)
    serializer_class = ApplicationTaskSerializer

    def get(self, request, app_id):
        applicationtasks = ApplicationTaskModel.objects.filter(application=app_id)
        #applicationtasks = ApplicationTaskModel.objects.all() 
        data = ApplicationTaskSerializer(applicationtasks, many=True).data
        print(data)
        return Response({ 'applicationtasks': data })

    def post(self, request, app_id, task_id):
        # """Create request"""
        # Add user to request data object

        request.data['applicationtask']['task'] = task_id
        request.data['applicationtask']['application'] = app_id

        # # Serialize/create task
        applicationtask = ApplicationTaskSerializer(data=request.data['applicationtask'])
        # If the college data is valid according to our serializer...
        if applicationtask.is_valid():
            # Save the created college & send a response
            applicationtask.save()
            return Response({ 'applicationtask': applicationtask.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(applicationtask.errors, status=status.HTTP_400_BAD_REQUEST)

class ApplicationTaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the applicationtask to show
        applicationtask = get_object_or_404(ApplicationTaskModel, pk=pk)
        # Only want to show owned tasks?
        # if request.user != applicationtask.owner:
        #     raise PermissionDenied('Unauthorized, you do not own this applicationtask')

        # Run the data through the serializer so it's formatted
        data = ApplicationTaskSerializer(applicationtask).data
        return Response({ 'applicationtask': data })

    # Nope cascade won't allow it. Do_nothing doesn't work either.
    def delete(self, request, pk):
        """Delete request"""
        # Locate applicationtask to delete
        applicationtask = get_object_or_404(ApplicationTaskModel, pk=pk)
        # Check the application task's owner against the user making this request
        # if request.user != applicationtask.owner:
        #     raise PermissionDenied('Unauthorized, you do not own this task')
        # Only delete if the user owns the trackcollege
        applicationtask.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate ApplicationTask
        # get_object_or_404 returns a object representation of our TrackCollege
        applicationtask = get_object_or_404(ApplicationTaskModel, pk=pk)
        # Check the application task's owner against the user making this request
        # if request.user != applicationtask.owner:
        #     raise PermissionDenied('Unauthorized, you do not own this applicationtask')

        # Ensure the owner field is set to the current user's ID
        # request.data['applicationtask']['owner'] = request.user.id
        # Validate updates with serializer
        data = ApplicationTaskSerializer(applicationtask, data=request.data['applicationtask'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

