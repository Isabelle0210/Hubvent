from django.urls import path

from Events.views.event import EventView

urlpatterns = [
     path('CreatedEvents/', EventView.as_view()), #metodo para criar um evento
     path('Events/', EventView.as_view()), #metodo para listar todos os eventos
     path('Events/<int:event_id>/', EventView.as_view()), #metodo para editar um evento
     
     #subscription
     
     path('Events/<int:event_id>/subscription/', EventView.as_view()), #metodo para se inscrever em um evento
     path('Events/subscription/<int:event_id>/', EventView.as_view()), #metodo para listar as inscrições de um evento
     path('Events/subscription/<int:event_id>/delete/', EventView.as_view()), #metodo para cancelar a inscrição de um evento
     
]