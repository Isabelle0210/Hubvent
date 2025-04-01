from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from BackEnd import Events
from Events.serializer import EventSubscriptionSerializer
from Events.models import EventSubscription
from rest_framework import status

import qrcode
import io
import base64

class SubscriptionToEventView(APIView):
     authentication_classes = [IsAuthenticated]

     def post (self,request, event_id):
          # caso o evento não exista, retorna um erro 404
          try :
               event = Events.objects.get(id=event_id)
          except Events.DoesNotExist:
               return Response({"error": "Evento não encontrado"}, status=404)
          
          # caso voce tente se inscrever em um evento que ja esta inscrito, retorna um erro 400
          if EventSubscription.objects.filter(event=event, user=request.user).exists():
               return Response({"error": "Você já está inscrito neste evento"}, status=400)
          
          
          #cria a inscrição no evento
          
          subscription = EventSubscription.objects.create(event=event, user=request.user)
          subscription.save()
          
          serializer = EventSubscriptionSerializer(subscription) # Aqui você deve usar o serializer correto para a inscrição
          
          
          # Aqui você pode gerar o QR code com os dados da inscrição
          qr_data = f"Inscrição ID: {subscription.id} - Evento: {event.title} - Usuário: {request.user.username}"
          qr = qrcode.make (qr_data)
          
          buffer = io.BytesIO()
          qr.save(buffer, format="PNG")
          qr.base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
          
          return Response({
               'subscription': serializer.data,
               'qr_code': qr.base64
          }, status=201)
          
     def get(self, request, event_id):
          try :
               event = Events.objects.get(id=event_id)
          except Events.DoesNotExist:
               return Response({"error": "Evento não encontrado"}, status=404)
          
          # Aqui você pode filtrar as inscrições do evento
          subscriptions = EventSubscription.objects.filter(event=event)
          serializer = EventSubscriptionSerializer(subscriptions, many=True)
          return Response({'subscriptions': serializer.data}, status=200)
     
     def delete (self, request, event_id):
          try:
               event = Events.objects.get(id=event_id)
          except Events.DoesNotExist:
               return Response({"error": "Evento não encontrado"}, status=404)
          
          # Verifica se a inscrição existe
          try:
               subscription = EventSubscription.objects.get(event=event, user=request.user)
          except EventSubscription.DoesNotExist:
               return Response({"error": "Inscrição não encontrada"}, status=404)
          
          # Deleta a inscrição
          subscription.delete()
          return Response({"message": "Inscrição cancelada com sucesso"}, status=204)
     