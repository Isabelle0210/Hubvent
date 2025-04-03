from rest_framework import serializers
from .models import Event, EventSubscription
from Users.models import User

from rest_framework import serializers
from Events.models import Event

class EventSerializer(serializers.ModelSerializer):
     created_by = serializers.ReadOnlyField(source='created_by.username')
     date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=True)

     class Meta:
          model = Event
          fields = ['title', 'description', 'date', 'created_by', 'created_at']

          
class EventSubscriptionSerializer(serializers.ModelSerializer):
     user = serializers.ReadOnlyField(source=User.nome)
     
     class Meta:
          model = EventSubscription
          fields = '__all__'
          
class SubscriptionCreateSerializer(serializers.ModelSerializer):
     class Meta:
          model = EventSubscription
          fields = 'Event'
          
     def create(self, validated_data):
          user = self.context['request'].user
          event = validated_data['event']
          
          if EventSubscription.objects.filter(event=event, user=user).exists():
               raise serializers.ValidationError('Você já está inscrito neste evento')
          
          return EventSubscription.objects.create(event=event, user=user)