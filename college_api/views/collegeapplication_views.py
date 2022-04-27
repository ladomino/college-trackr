from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.collegeapplication import CollegeApplication as CollegeApplicationModel
from ..serializers import CollegeApplicationSerializer, CollegeApplicationReadSerializer

# Create your views here.
class CollegeApplicationList(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = CollegeApplicationSerializer

    def get(self, request, app_id):
        """Index request"""
        # Get all the applications:
        # applications = Application.objects.all()
        # Filter the applications by owner, so you can only see your owned 
        # applications
        collegeapplications = CollegeApplicationModel.objects.filter(application=app_id)
        # Run the data through the serializer
        data = CollegeApplicationSerializer(collegeapplications, many=True).data
        return Response({ 'collegeapplications': data })

    def post(self, request, college_id, app_id):
        """Create request"""
        # Add user to request data object
        request.data['collegeapplication']['college'] = college_id
        request.data['collegeapplication']['application'] = app_id
      
        # Serialize/create application
        collegeapplication = CollegeApplicationSerializer(data=request.data['collegeapplication'])
        # If the application data is valid according to our serializer...
        if collegeapplication.is_valid():
            # Save the created application & send a response
            collegeapplication.save()
            return Response({ 'collegeapplication': collegeapplication.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(application.errors, status=status.HTTP_400_BAD_REQUEST)

class CollegeApplicationDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the application to show
        collegeapplication = get_object_or_404(CollegeApplicationModel, pk=pk)
        # Only want to show owned applications
        # if request.user != collegeapplication.owner:
        #     raise PermissionDenied('Unauthorized, you do not own this application')

        # Run the data through the serializer so it's formatted
        data = CollegeApplicationSerializer(collegeapplication).data
        return Response({ 'collegeapplication': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate application to delete
        collegeapplication = get_object_or_404(CollegeApplicationModel, pk=pk)
        # Check the application's owner against the user making this request
        # if request.user != collegeapplication.owner:
        #     raise PermissionDenied('Unauthorized, you do not own this application')
        # Only delete if the user owns the  application
        collegeapplication.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate Application
        # get_object_or_404 returns a object representation of our Application
        collegeapplication = get_object_or_404(CollegeApplicationModel, pk=pk)
        # Check the application's owner against the user making this request
        # if request.user != collegeapplication.owner:
        #     raise PermissionDenied('Unauthorized, you do not own this application')

        # Ensure the owner field is set to the current user's ID
        # request.data['collegeapplication']['owner'] = request.user.id
        # Validate updates with serializer
        data = CollegeApplicationSerializer(collegeapplication, data=request.data['collegeapplication'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)