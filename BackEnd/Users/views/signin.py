from Users.auth import Authentication
from Users.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

class Signin(APIView):
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