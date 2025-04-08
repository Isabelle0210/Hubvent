from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from Events.models import Event
from Events.serializer import EventSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.utils.timezone import now
from django.utils.timezone import now, make_aware
from dateutil.parser import parse, ParserError
import datetime



class EventView(APIView):
     permission_classes = [IsAuthenticated]

     @swagger_auto_schema(
          operation_summary="Criar Evento",
          request_body=openapi.Schema(
               type=openapi.TYPE_OBJECT,
               properties={
                    'title': openapi.Schema(type=openapi.TYPE_STRING),
                    'description': openapi.Schema(type=openapi.TYPE_STRING),
                    'date': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME)
               }
          ),
          responses={
               201: "Evento criado com sucesso",
               400: "Dados insuficientes ou inválidos",
               403: "Permissão negada"
          }
     )
     


     def post(self, request):
          title = request.data.get('title')
          description = request.data.get('description')
          date = request.data.get('date')

          if not title or not description or not date:
               return Response({"error": "Dados insuficientes"}, status=status.HTTP_400_BAD_REQUEST)

          try:
               event_date = parse(date)  # Converte para datetime
               event_date = make_aware(event_date)  # 🛠️ Garante que tem timezone
               if event_date.tzinfo is None:  # Se for 'naive', tornamos 'aware'
                    event_date = make_aware(event_date)
          except ParserError:
               return Response({"error": "Data inválida"}, status=status.HTTP_400_BAD_REQUEST)

          if event_date < now():  # Aqui ambas as datas serão "timezone-aware"
               return Response({"error": "A data deve ser no futuro"}, status=status.HTTP_400_BAD_REQUEST)

          event = Event.objects.create(
               title=title,
               description=description,
               date=event_date,
               created_by=request.user
          )

          serializer = EventSerializer(event)
          return Response({'event': serializer.data}, status=status.HTTP_201_CREATED)

     
class ListEventView(APIView):
     permission_classes = [IsAuthenticated]
     @swagger_auto_schema(
          operation_summary="Listar Eventos",
          responses={
               200: "Lista de eventos retornada com sucesso",
               500: "Erro interno do servidor"
          }
     )
     def get(self, request):
          events = Event.objects.filter(date__isnull=False)  # Ignora os sem data
          serializer = EventSerializer(events, many=True)
          return Response({'events': serializer.data}, status=status.HTTP_200_OK)

class UpdateEventView(APIView):
     permission_classes = [IsAuthenticated]
    
     @swagger_auto_schema(
          operation_summary="Atualizar Evento",
          request_body=openapi.Schema(
               type=openapi.TYPE_OBJECT,
               properties={
                    'title': openapi.Schema(type=openapi.TYPE_STRING),
                    'description': openapi.Schema(type=openapi.TYPE_STRING)
               }
          ),
          responses={
               200: "Evento atualizado com sucesso",
               400: "Dados insuficientes",
               403: "Permissão negada",
               404: "Evento não encontrado"
          }
     )
     def put(self, request, event_id):
          try:
               event = Event.objects.get(id=event_id)
          except Event.DoesNotExist:
               return Response({"error": "Evento não encontrado"}, status=status.HTTP_404_NOT_FOUND)

        # Garantir que o usuário autenticado seja o criador do evento
          if event.created_by_id != request.user.id:
               return Response({"error": "Você não tem permissão para editar este evento"}, status=status.HTTP_403_FORBIDDEN)
        
        # Pega apenas os campos permitidos
          allowed_fields = {key: request.data[key] for key in ["title", "description"] if key in request.data}
        
          if not allowed_fields:
               return Response({"error": "Nenhum campo permitido foi enviado"}, status=status.HTTP_400_BAD_REQUEST)
        
          serializer = EventSerializer(event, data=allowed_fields, partial=True)
          if serializer.is_valid():
               serializer.save()
               return Response({'event': serializer.data}, status=status.HTTP_200_OK)
        
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)