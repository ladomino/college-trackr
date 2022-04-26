from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView, DeleteView

from ..models.trackcollege import TrackCollege as TrackCollegeModel
from ..serializers import TrackCollegeSerializer

class TrackCollegeList(generics.ListCreateAPIView):
    
    permission_classes=(IsAuthenticated,)
    serializer_class = TrackCollegeSerializer

    def get(self, request):
        trackcolleges = TrackCollegeModel.objects.all()
        data = TrackCollegeSerializer(trackcolleges, many=True).data
        return Response({ 'trackcolleges': data })

    def post(self, request, college_id):
        # """Create request"""
        # Add user to request data object

        request.data['trackcollege']['owner'] = request.user.id
        request.data['trackcollege']['college'] = college_id

        # # Serialize/create task
        trackcollege = TrackCollegeSerializer(data=request.data['trackcollege'])
        # If the college data is valid according to our serializer...
        if trackcollege.is_valid():
            # Save the created college & send a response
            trackcollege.save()
            return Response({ 'trackcollege': trackcollege.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(trackcollege.errors, status=status.HTTP_400_BAD_REQUEST)

class TrackCollegeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the trackcollege to show
        trackcollege = get_object_or_404(TrackCollegeModel, pk=pk)
        # Only want to show owned tasks?
        if request.user != trackcollege.owner:
            raise PermissionDenied('Unauthorized, you do not own this task')

        # Run the data through the serializer so it's formatted
        data = TrackCollegeSerializer(trackcollege).data
        return Response({ 'trackcollege': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate trackcollege to delete
        trackcollege = get_object_or_404(TrackCollegeModel, pk=pk)
        # Check the task's owner against the user making this request
        if request.user != trackcollege.owner:
            raise PermissionDenied('Unauthorized, you do not own this task')
        # Only delete if the user owns the trackcollege
        trackcollege.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate TrackCollege
        # get_object_or_404 returns a object representation of our TrackCollege
        trackcollege = get_object_or_404(TrackCollegeModel, pk=pk)
        # Check the task's owner against the user making this request
        if request.user != trackcollege.owner:
            raise PermissionDenied('Unauthorized, you do not own this task')

        # Ensure the owner field is set to the current user's ID
        request.data['trackcollege']['owner'] = request.user.id
        # Validate updates with serializer
        data = TrackCollegeSerializer(trackcollege, data=request.data['trackcollege'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)