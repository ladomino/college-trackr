from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.college import College as CollegeModel
from ..models.trackcollege import TrackCollege as TrackCollegeModel
from ..serializers import CollegeSerializer, CollegeReadSerializer, TrackCollegeSerializer


# Retrieve a list of colleges.
class CollegeList(generics.ListCreateAPIView):
    
    permission_classes=(IsAuthenticated,)
    serializer_class = CollegeSerializer

    def get(self, request):
        # colleges = CollegeModel.objects.all()

        # This will get all colleges tracked by a user
        colleges = CollegeModel.objects.filter(track_colleges=request.user.id)

        data = CollegeReadSerializer(colleges, many=True).data
        print(data)
        return Response({ 'colleges': data })

    def post(self, request):
        # """Create request"""
        # Add user to request data object
        # request.data['college']['owner'] = request.user.id
        # # Serialize/create college
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
        print(college.track_colleges.all().values())

        # Only want to show owned college?
        # if request.user != college.owner:
        #     raise PermissionDenied('Unauthorized, you do not own this college')

        # Run the data through the serializer so it's formatted
        data = CollegSerializer(college).data
        print(data)

        return Response({ 'college': data })

class CollegeUnTrackList(generics.ListCreateAPIView):
    
    permission_classes=(IsAuthenticated,)
    serializer_class = CollegeSerializer

    def get(self, request):
        # colleges = CollegeModel.objects.all()

        # This will get all colleges nottracked by a user
        colleges = CollegeModel.objects.exclude(track_colleges = request.user.id)
        print(colleges)

        data = CollegeSerializer(colleges, many=True).data
        print(data)
        return Response({ 'colleges': data })
