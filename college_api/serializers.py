from django.contrib.auth import get_user_model
from college_api.models.applicationtask import ApplicationTask
from rest_framework import serializers

from .models.application import Application
from .models.college import College
from .models.collegeapplication import CollegeApplication
from .models.trackcollege import TrackCollege
from .models.task import Task
from .models.applicationtask import ApplicationTask
from .models.user import User


class TrackCollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackCollege
        fields = ('id', 'status', 'college', 'owner')

class CollegeSerializer(serializers.ModelSerializer):
    #track_colleges = TrackCollegeSpecificSerializer(many=True)
    class Meta:
        model = College
        fields = ('id', 'name', 'city', 'state', 'image', 'early_decision', 'early_action', 'regular_decision', 
        'app_home_link', 'track_colleges')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'mandatory')


class CollegeApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeApplication
        fields = ('id', 'date_submitted', 'in_progress', 'hold', 'early_decision', 'early_action', 'regular_decision')       

class ApplicationTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationTask
        fields = ('id', 'importance', 'due_date', 'complete', 'working_on', 'application', 'task')

class ApplicationSerializer(serializers.ModelSerializer):
    college_applications = CollegeApplicationSerializer(many=True)
    #application_tasks = ApplicationTaskSerializer(many=True) only for when applicationtaskserializer
    # did not have the columns.
    class Meta:
        model = Application
        fields = ('id', 'name', 'link', 'created', 'owner', 'college_applications', 'application_tasks')


class UserSerializer(serializers.ModelSerializer):    
    # This model serializer will be used for User creation
    # The login serializer also inherits from this serializer
    # in order to require certain data for login
    class Meta:
        # get_user_model will get the user model (this is required)
        # https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#referencing-the-user-model
        model = get_user_model()
        fields = ('id', 'email', 'password')
        extra_kwargs = { 'password': { 'write_only': True, 'min_length': 5 } }

    # This create method will be used for model creation
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

class UserRegisterSerializer(serializers.Serializer):
    # Require email, password, and password_confirmation for sign up
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True)
    password_confirmation = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        # Ensure password & password_confirmation exist
        if not data['password'] or not data['password_confirmation']:
            raise serializers.ValidationError('Please include a password and password confirmation.')

        # Ensure password & password_confirmation match
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError('Please make sure your passwords match.')
        # if all is well, return the data
        return data

class ChangePasswordSerializer(serializers.Serializer):
    model = get_user_model()
    old = serializers.CharField(required=True)
    new = serializers.CharField(required=True)

