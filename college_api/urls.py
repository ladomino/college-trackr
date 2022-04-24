from django.urls import path
#from .views.mango_views import Mangos, MangoDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
  	# Restful routing
    path('signup/', SignUp.as_view(), name='sign-up'),
    path('login/', SignIn.as_view(), name='sign-in'),
    path('logout/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
