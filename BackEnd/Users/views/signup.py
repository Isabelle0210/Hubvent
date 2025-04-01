from Users.auth import Authentication
from Users.serializers import UserSerializer
from Users.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Signup(APIView):
     def post(self, request):
          nome = request.data.get("nome")
          email = request.data.get("email")
          password = request.data.get("password")

          if not nome or not email or not password:
               return Response({"error": "Dados insuficientes"}, status=status.HTTP_400_BAD_REQUEST)

          # Verifica se o e-mail já está cadastrado
          if User.objects.filter(email=email).exists():
               return Response({"error": "E-mail já cadastrado"}, status=status.HTTP_400_BAD_REQUEST)

          # Criando usuário via Authentication.signup()
          user = Authentication.signup(nome, email, password)

          if not user:
               return Response({"error": "Erro ao criar usuário"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

          serializer = UserSerializer(user)
          return Response({"user": serializer.data}, status=status.HTTP_201_CREATED)
