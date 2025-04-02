from django.shortcuts import get_object_or_404
from Users.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from Users.serializers import UserSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class UserView(APIView):
     permission_classes = [IsAuthenticated]
     
     @swagger_auto_schema(
          operation_summary="Detalhes do Usuário",
          responses={
               200: openapi.Response('Usuário encontrado'),
               404: openapi.Response('Usuário não encontrado')
          }
     )
     
     def get(self, request, user_id):  # Agora o método recebe user_id
          user = get_object_or_404(User, id=user_id)
          serializer = UserSerializer(user)
          return Response(serializer.data, status=200)
     
     
     