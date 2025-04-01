

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from BackEnd import Events
from Events.serializer import EventSerializer


class EventView(APIView):
     permission_classes = [IsAuthenticated]
     def post (self, request) -> None:
          title = request.data.get("title")
          description = request.data.get("description")
          date = request.data.get("date")
          created_by = request.user.id # AQUI PEGA O ID DO USUARIO LOGADO QUE ESTA CRIANDO O EVENTO
          created_at = request.data.get("created_at") #DATA QUE O EVENTO FOI CRIADO
          
          if not title or not description or not date:
               return Response({"error": "Dados insuficientes"}, status=400)
          
          # Aqui você deve adicionar a lógica para criar o evento no banco de dados
          
          event = Events.objects.create(
               title=title,
               description=description,
               created_by=created_by,
               created_at=created_at
          )
          event.save()
          
          serializer = EventSerializer(event) # Aqui você deve usar o serializer correto para o evento
          
          return Response({'event':serializer.data}, status=201)
     
     def get(self, request):
          events = Events.objects.all()
          serializer = EventSerializer(events, many=True)
          
          return Response({'events': serializer.data}, status=200)
     
     def put(self, request, event_id):
          try:
               event = Events.objects.get(id=event_id)
          except Events.DoesNotExist:
               return Response({"error": "Evento não encontrado"}, status=status.HTTP_404_NOT_FOUND)

          # Garantir que o usuário autenticado seja o criador do evento
          if event.created_by != request.user:
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
          