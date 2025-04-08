import datetime
from rest_framework import serializers
from .models import Event, EventSubscription
from Users.models import User

class EventSerializer(serializers.ModelSerializer):
     class Meta:
          model = Event
          fields = '__all__'

     def to_representation(self, instance):
          rep = super().to_representation(instance)
          if rep.get('date') is None:
               rep['date'] = ''  # ou qualquer valor default, como 'Data indefinida'
          return rep



class EventSubscriptionSerializer(serializers.ModelSerializer):
     user = serializers.ReadOnlyField(source='user.nome')  # corrigido
     class Meta:
          model = EventSubscription
          fields = '__all__'

class SubscriptionCreateSerializer(serializers.ModelSerializer):
     class Meta:
          model = EventSubscription
          fields = ['event']

     def create(self, validated_data):
          user = self.context['request'].user
          event = validated_data['event']

          if EventSubscription.objects.filter(event=event, user=user).exists():
               raise serializers.ValidationError('Você já está inscrito neste evento')

          return EventSubscription.objects.create(event=event, user=user)
