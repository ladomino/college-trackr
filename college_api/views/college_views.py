from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.college import College
from ..serializers import CollegeSerializer

class CollegeList(generics.ListAPIView):
    
    permission_classes=(IsAuthenticated,)
    serializer_class = CollegeSerializer

    def get(self, request):
        colleges = College.object.all()
        data = CollegeSerializer(colleges, many=True).data
        return Response({ 'colleges': data })
