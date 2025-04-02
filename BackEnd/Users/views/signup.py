from Users.auth import Authentication
from Users.serializers import UserSerializer
from Users.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class Signup(APIView):
     
     @swagger_auto_schema(
          operation_summary="Cadastro de Usuário",
          request_body=openapi.Schema(
               type=openapi.TYPE_OBJECT,
               properties={
                    'nome': openapi.Schema(type=openapi.TYPE_STRING, description='Nome do usuário'),
                    'email': openapi.Schema(type=openapi.TYPE_STRING, description='E-mail do usuário'),
                    'password': openapi.Schema(type=openapi.TYPE_STRING, description='Senha do usuário')
               },
               required=['nome', 'email', 'password']
          ),
          responses={
               201: openapi.Response('Usuário criado com sucesso'),
               400: openapi.Response('Dados insuficientes ou e-mail já cadastrado'),
               500: openapi.Response('Erro ao criar usuário')
          }
     )
     
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
