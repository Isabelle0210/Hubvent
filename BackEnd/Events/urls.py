from django.urls import path

from Events.views.subscription import DeleteSubscriptionView, ListSubscriptionView, SubscriptionToEventView
from Events.views.event import EventView, ListEventView, UpdateEventView

urlpatterns = [
     path('CreatedEvents/', EventView.as_view(), name = 'cria-eventos'), #metodo para criar um evento
     path('', ListEventView.as_view(), name= 'lista-eventos'), #metodo para listar todos os eventos
     path('<int:event_id>/', UpdateEventView.as_view(), name='edita-evento'), #metodo para editar um evento
     
     #subscription
     
     path('<int:event_id>/subscription/', SubscriptionToEventView.as_view(), name = 'subscripition'), #metodo para se inscrever em um evento
     path('subscription/<int:event_id>/', ListSubscriptionView.as_view(), name = 'lista-evento'), #metodo para listar as inscrições de um evento
     path('subscription/<int:event_id>/delete/', DeleteSubscriptionView.as_view(), name = 'cancela-evento'), #metodo para cancelar a inscrição de um evento
     
]