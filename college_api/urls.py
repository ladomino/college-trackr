from django.urls import path
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword
from .views.college_views import CollegeList, CollegeDetail
from .views.application_views import ApplicationList, ApplicationDetail
from .views.task_views import TaskList, TaskDetail
from .views.trackcollege_views import TrackCollegeList, TrackCollegeDetail
from .views.applicationtask_views import ApplicationTaskList, ApplicationTaskDetail
from .views.collegeapplication_views import CollegeApplicationList, CollegeApplicationDetail


urlpatterns = [
    # path('collegetkr/', views.index, name='index'),
    # path('collegetkr/about/', views.about, name='about'),

    path('collegetkr/colleges/', CollegeList.as_view(), name='college'),
    # college details button
    path('collegetkr/colleges/<int:pk>/', CollegeDetail.as_view(), name='college_detail'),
    # create button
    path('collegetkr/colleges/create/', CollegeList.as_view(), name='college_create'),
    # track button
    path('collegetkr/colleges/<int:college_id>/track/', TrackCollegeList.as_view(), name='college_track'),
    # track your colleges
    path('collegetkr/collegetrack/', TrackCollegeList.as_view(), name='college_track_show'),
    path('collegetkr/collegetrack/<int:pk>/', TrackCollegeDetail.as_view(), name='college_track_detail'),
    
    path('collegetkr/apps/<int:college_id>/assign/<int:app_id>/', CollegeApplicationList.as_view(), name='collegeapp_assign_task'),
    path('collegetkr/collegeapps/<int:pk>/update/', CollegeApplicationDetail.as_view(), name='collegeapp_update'),
    path('collegetkr/collegeapps/<int:pk>/delete/', CollegeApplicationDetail.as_view(), name='colllegeapp_delete'),

    # path('collegetkr/apps/<int:college_id>', views.apps_detail, name='app_detail'),

    # applications
    path('collegetkr/apps/', ApplicationList.as_view(), name='apps_index'),
    path('collegetkr/apps/<int:pk>/', ApplicationDetail.as_view(), name='app_detail'),
    path('collegetkr/apps/<int:college_id>/create/', ApplicationList.as_view(), name='app_create'),
    path('collegetkr/apps/<int:pk>/update/', ApplicationDetail.as_view(), name='app_update'),
    path('collegetkr/apps/<int:pk>/delete/', ApplicationDetail.as_view(), name='app_delete'),

    path('collegetkr/tasks/', TaskList.as_view(), name='task_index'),
    path('collegetkr/tasks/<int:app_id>/', ApplicationTaskList.as_view(), name='app_task_index'),
    path('collegetkr/tasks/create/', TaskList.as_view(), name='create_task'),
    path('collegetkr/tasks/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    path('collegetkr/apptasks/<int:app_id>/', ApplicationTaskList.as_view(), name='app_tasks_show'),
    #path('collegetkr/apptasks/', ApplicationTaskList.as_view(), name='app_tasks_show'),
    path('collegetkr/apptasks/<int:app_id>/assign/<int:task_id>/', ApplicationTaskList.as_view(), name='assign_task'),
    path('collegetkr/apptasks/<int:pk>/', ApplicationTaskDetail.as_view(), name='remove_task'),
  	# Restful routing
    path('signup/', SignUp.as_view(), name='sign-up'),
    path('login/', SignIn.as_view(), name='sign-in'),
    path('logout/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
