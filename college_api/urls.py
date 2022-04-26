from django.urls import path
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword
from .views.college_views import CollegeList, CollegeDetail
from .views.application_views import ApplicationList, ApplicationDetail
from .views.task_views import TaskList, TaskDetail
from .views.trackcollege_views import TrackCollegeList, TrackCollegeDetail

urlpatterns = [
    # path('collegetkr/', views.index, name='index'),
    # path('collegetkr/about/', views.about, name='about'),

    path('collegetkr/colleges/', CollegeList.as_view(), name='college'),
    path('collegetkr/colleges/<int:pk>/', CollegeDetail.as_view(), name='college_detail'),
    path('collegetkr/colleges/create/', CollegeList.as_view(), name='college'),
    path('collegetkr/colleges/<int:college_id>/track/', TrackCollegeList.as_view(), name='college_track'),
    path('collegetkr/collegetrack/', TrackCollegeList.as_view(), name='college_track_show'),
    path('collegetkr/collegetrack/<int:pk>/', TrackCollegeDetail.as_view(), name='college_track_detail'),
    path('collegetkr/apps/', ApplicationList.as_view(), name='apps_index'),
    # path('collegetkr/apps/<int:college_id>', views.apps_detail, name='app_detail'),
    path('collegetkr/apps/<int:college_id>/create/', ApplicationList.as_view(), name='app_create'),
    path('collegetkr/apps/<int:pk>/update/', ApplicationDetail.as_view(), name='app_update'),
    path('collegetkr/apps/<int:pk>/delete/', ApplicationDetail.as_view(), name='app_delete'),
    path('collegetkr/tasks/', TaskList.as_view(), name='task_index'),
    # path('collegetkr/tasks/<int:app_id>', views.app_task_index, name='app_task_index'),
    path('collegetkr/tasks/create/', TaskList.as_view(), name='create_task'),
    path('collegetkr/tasks/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    # path('collegetkr/tasks/<int:app_id>/assign/<int:task_id>', views.assign_task, name='assign_task'),
    # path('collegetkr/tasks/<int:app_id>/remove/<int:task_id>', views.remove_task, name='remove_task'),
  	# Restful routing
    path('signup/', SignUp.as_view(), name='sign-up'),
    path('login/', SignIn.as_view(), name='sign-in'),
    path('logout/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
