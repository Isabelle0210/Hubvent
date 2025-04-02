from Users.auth import Authentication
from Users.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class Signin(APIView):
     
     @swagger_auto_schema(
          operation_summary="Login de Usuário",
          request_body=openapi.Schema(
               type=openapi.TYPE_OBJECT,
               properties={
                    'email': openapi.Schema(type=openapi.TYPE_STRING),
                    'password': openapi.Schema(type=openapi.TYPE_STRING)
               }
          ),
          responses={
               200: "Usuário autenticado com sucesso",
               400: "Dados insuficientes",
               401: "Credenciais inválidas"
          }
     )
     
     def post(self, request) -> None:
          email = request.data.get("email")
          password = request.data.get("password")
          
          if not email or not password:
               return Response({"error": "Dados insuficientes"}, status=400)
          
          user = Authentication.signin(email, password)
          serializer = UserSerializer(user)
          
          refresh = RefreshToken.for_user(user)
          
          return Response({"user": 
               serializer.data, 
               "refresh": str(refresh), 
               "access": str(refresh.access_token)}, 
                         status=200)