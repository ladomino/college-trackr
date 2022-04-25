from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.application import Application
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
        applications = Application.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = ApplicationSerializer(applications, many=True).data
        return Response({ 'applications': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['application']['owner'] = request.user.id
        # Serialize/create mango
        application = ApplicationSerializer(data=request.data['application'])
        # If the mango data is valid according to our serializer...
        if application.is_valid():
            # Save the created mango & send a response
            application.save()
            return Response({ 'application': application.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(application.errors, status=status.HTTP_400_BAD_REQUEST)

# class MangoDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes=(IsAuthenticated,)
#     def get(self, request, pk):
#         """Show request"""
        # Locate the mango to show
        # mango = get_object_or_404(Mango, pk=pk)
        # Only want to show owned mangos?
        # if request.user != mango.owner:
        #     raise PermissionDenied('Unauthorized, you do not own this mango')

        # Run the data through the serializer so it's formatted
    #     data = MangoSerializer(mango).data
    #     return Response({ 'mango': data })

    # def delete(self, request, pk):
        # """Delete request"""
        # Locate mango to delete
        # mango = get_object_or_404(Mango, pk=pk)
        # Check the mango's owner against the user making this request
        # if request.user != mango.owner:
            # raise PermissionDenied('Unauthorized, you do not own this mango')
        # Only delete if the user owns the  mango
        # mango.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)

    # def partial_update(self, request, pk):
    #     """Update Request"""
        # Locate Mango
        # get_object_or_404 returns a object representation of our Mango
        # mango = get_object_or_404(Mango, pk=pk)
        # Check the mango's owner against the user making this request
        # if request.user != mango.owner:
        #     raise PermissionDenied('Unauthorized, you do not own this mango')

        # Ensure the owner field is set to the current user's ID
        # request.data['mango']['owner'] = request.user.id
        # Validate updates with serializer
        # data = MangoSerializer(mango, data=request.data['mango'], partial=True)
        # if data.is_valid():
            # Save & send a 204 no content
            # data.save()
            # return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        # return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
