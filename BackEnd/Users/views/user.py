from django.shortcuts import get_object_or_404
from Users.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from Users.serializers import UserSerializer

class UserView(APIView):
     permission_classes = [IsAuthenticated]
     
     def get(self, request, user_id):  # Agora o método recebe user_id
          user = get_object_or_404(User, id=user_id)
          serializer = UserSerializer(user)
          return Response(serializer.data, status=200)
     
     
     