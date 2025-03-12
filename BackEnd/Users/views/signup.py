from Users.auth import Authentication
from Users.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class Signup(APIView):
     def post (self, request) -> None:
          nome = request.data.get("nome")
          email = request.data.get("email")
          password = request.data.get("password")
          
          if not nome or not email or not password:
               return Response({"error": "Dados insuficientes"}, status=400)
          
          user = Authentication.signup(nome, email, password)
          serializer = UserSerializer(user)
          
          return Response({"user": serializer.data}, status=201)
     
     
     
