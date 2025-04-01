

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from Events.models import Event
from Events.serializer import EventSerializer


class EventView(APIView):
     permission_classes = [IsAuthenticated]
     def post(self, request):
          title = request.data.get("title")
          description = request.data.get("description")

          if not title or not description:
               return Response({"error": "Dados insuficientes"}, status=status.HTTP_400_BAD_REQUEST)

          try:
               event = Event.objects.create(
                    title=title,
                    description=description,
                    created_by=request.user,  # Passando o usuário inteiro, não só o ID
                    created_at=now()  # Usa o timestamp atual
               )
               serializer = EventSerializer(event)
               return Response(serializer.data, status=status.HTTP_201_CREATED)
          except Exception as e:
               return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
     
     def get(self, request):
          events = Event.objects.all()
          serializer = EventSerializer(events, many=True)
          
          return Response({'events': serializer.data}, status=200)
     
     def put(self, request, event_id):
          try:
               event = Event.objects.get(id=event_id)
          except Event.DoesNotExist:
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
          