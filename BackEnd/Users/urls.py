
from django.urls import path

from Users.views.signin import Signin
from Users.views.signup import Signup
from Users.views.user import UserView

urlpatterns = [
     path('signin/', Signin.as_view()),
     path('signup/', Signup.as_view()),
     path('get_users/', UserView.as_view()),
     path('get_user/<int:user_id>/', UserView.as_view(), name='get_user') #metodo para pesquisar um usuario especifico pelo id
]