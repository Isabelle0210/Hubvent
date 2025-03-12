from rest_framework import serializers

from Users.models import User

class UserSerializer(serializers.ModelSerializer):
     class Meta:
          model = User
          fields = ["id", "nome", "email", "is_owner", "is_active", "date_joined"]
          
          
          