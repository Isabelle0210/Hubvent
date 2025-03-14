
from django.urls import path

from Users.views.signin import Signin
from Users.views.signup import Signup
from Users.views.user import UserView

urlpatterns = [
     path('signin/', Signin.as_view()),
     path('signup/', Signup.as_view()),
     path('user/', UserView.as_view()),
]