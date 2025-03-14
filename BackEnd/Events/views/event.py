from rest_framework import viewsets, permissions, generics
from Events.models import Event, Subscription
from Events.permissions import IsAdminOrReadOnly
from Events.serializer import EventSerializer, SubscriptionCreateSerializer, SubscriptionSerializer


class EventViewSet(viewsets.ModelViewSet): #viewset para eventos 
     queryset = Event.objects.all().order_by('date') #queryset de eventos ordenados por data
     serializer_class = EventSerializer #serializer de eventos 
     permission_classes = [IsAdminOrReadOnly] #permissões para eventos

     def perform_create(self, serializer): #cria um evento
          serializer.save(created_by=self.request.user)# salva o evento com o usuário autenticado

class SubscriptionViewSet(viewsets.ModelViewSet): # viewset para inscrições em eventos 
     queryset = Subscription.objects.all()
     serializer_class = SubscriptionSerializer
     permission_classes = [permissions.IsAuthenticated]

     def perform_create(self, serializer): #cria uma inscrição em um evento
          serializer.save(user=self.request.user)


class SubscribeToEventView(generics.CreateAPIView):
     serializer_class = SubscriptionCreateSerializer
     permission_classes = [permissions.IsAuthenticated]  # Apenas usuários logados podem se inscrever