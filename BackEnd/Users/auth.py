from rest_framework.exceptions import AuthenticationFailed, APIException
from Users.models import User
from django.contrib.auth.hashers import check_password, make_password

class Authentication:
     @staticmethod
     def signin(email=None, password=None):
          if not email or not password:
               raise AuthenticationFailed("Usuário ou senha inválidos")

          user = User.objects.filter(email=email).first()

          if not user or not check_password(password, user.password):
               raise AuthenticationFailed("Usuário ou senha inválidos")

          return user

     @staticmethod
     def signup(nome=None, email=None, password=None):
          if not nome:
               raise APIException("O nome é obrigatório")
          if not email:
               raise APIException("O email é obrigatório")
          if not password:
               raise APIException("A senha é obrigatória")

          hashed_password = make_password(password)

          created_user = User.objects.create(
               nome=nome,
               email=email,
               password=hashed_password
          )

          return created_user
