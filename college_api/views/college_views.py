from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.college import College as CollegeModel
from ..serializers import CollegeSerializer


# Retrieve a list of colleges.
class CollegeList(generics.ListCreateAPIView):
    
    #permission_classes=(IsAuthenticated,)
    serializer_class = CollegeSerializer

    def get(self, request):
        colleges = CollegeModel.objects.all()
        data = CollegeSerializer(colleges, many=True).data
        return Response({ 'colleges': data })

    def post(self, request):
        # """Create request"""
        # Add user to request data object
        # request.data['college']['owner'] = request.user.id
        # # Serialize/create mango
        college = CollegeSerializer(data=request.data['college'])
        # If the college data is valid according to our serializer...
        if college.is_valid():
            # Save the created college & send a response
            college.save()
            return Response({ 'college': college.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(college.errors, status=status.HTTP_400_BAD_REQUEST)

# Show a College via pk
class CollegeDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the college to show
        college = get_object_or_404(CollegeModel, pk=pk)
        # Only want to show owned mangos?
        # if request.user != mango.owner:
        #     raise PermissionDenied('Unauthorized, you do not own this mango')

        # Run the data through the serializer so it's formatted
        data = CollegeSerializer(college).data
        return Response({ 'college': data })