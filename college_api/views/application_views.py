from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.application import Application as ApplicationModel
from ..serializers import ApplicationSerializer


# Create your views here.
class ApplicationList(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = ApplicationSerializer

    def get(self, request):
        """Index request"""
        # Get all the applications:
        # applications = Application.objects.all()
        # Filter the applications by owner, so you can only see your owned 
        # applications
        applications = ApplicationModel.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = ApplicationSerializer(applications, many=True).data
        return Response({ 'applications': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['application']['owner'] = request.user.id
        # Serialize/create application
        application = ApplicationSerializer(data=request.data['application'])
        
        # If the application data is valid according to our serializer...
        if application.is_valid():
            # Save the created application & send a response
            application.save()
            return Response({ 'application': application.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(application.errors, status=status.HTTP_400_BAD_REQUEST)

class ApplicationDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the application to show
        application = get_object_or_404(ApplicationModel, pk=pk)
        # Only want to show owned applications
        if request.user != application.owner:
            raise PermissionDenied('Unauthorized, you do not own this application')

        # Run the data through the serializer so it's formatted
        data = ApplicationSerializer(application).data
        return Response({ 'application': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate application to delete
        application = get_object_or_404(ApplicationModel, pk=pk)
        # Check the application's owner against the user making this request
        if request.user != application.owner:
            raise PermissionDenied('Unauthorized, you do not own this application')
        # Only delete if the user owns the  application
        application.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate Application
        # get_object_or_404 returns a object representation of our Application
        application = get_object_or_404(ApplicationModel, pk=pk)
        # Check the application's owner against the user making this request
        if request.user != application.owner:
            raise PermissionDenied('Unauthorized, you do not own this application')

        # Ensure the owner field is set to the current user's ID
        request.data['application']['owner'] = request.user.id
        # Validate updates with serializer
        data = ApplicationSerializer(application, data=request.data['application'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

