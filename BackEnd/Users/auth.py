from rest_framework.exceptions import AuthenticationFailed, APIException
from Users.models import User
from django.contrib.auth.hashers import check_password, make_password

class Authentication:
     def signin(email = None, password= None):
          user_exists = User.objects.filter(email=email).exists()
          
          exception_auth = APIException("Usuário ou senha inválidos", status_code=401)
     
          if not user_exists:
               raise exception_auth
          
          user = User.objects.get(email=email).first()
          
          if not check_password(password, user.password):
               raise exception_auth
          
          return user
     def signup(nome = None, email = None, password = None):
          
          if not name or nome == "":
               raise APIException("O nome é obrigatório", status_code=400)
          
          if not email or email == "":
               raise APIException("O email é obrigatório", status_code=400)
          
          if not password or password == "":
               raise APIException("A senha é obrigatória", status_code=400)
          
          password_bash = make_password(password)
          
          created_user = User.objects.create(
               nome=nome, 
               email=email, 
               password=password_bash
               
          )
          return created_user