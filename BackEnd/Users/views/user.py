from Users.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from Users.serializers import UserSerializer

class UserView(APIView):
     permission_classes = [IsAuthenticated]
     
     def get (self, request) -> None:
          users = User.objects.all()
          serializer = UserSerializer(users, many=True)
          return Response({"users": serializer.data}, status=200)
     
     