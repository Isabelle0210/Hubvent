from django.db import models
from Users.models import User

# Create your models here.


class Event(models.Model): # modelo de como um evento deve ser e como ele deve ser salvo no banco de dados
     title = models.CharField(max_length=100)
     description = models.TextField()
     date = models.DateTimeField()
     created_at = models.DateTimeField(auto_now_add=True) 
     created_by = models.ForeignKey(User, on_delete=models.CASCADE)
     
     def __str__(self):
          return self.title
     
class EventSubscription(models.Model): # modelo de como uma inscrição deve ser e como ela deve ser salva no banco de dados
     event = models.ForeignKey(Event, on_delete=models.CASCADE)
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     subscribed_at = models.DateTimeField(auto_now_add=True)
     
     class Meta:
          unique_together = ('event', 'user')
          
     def __str__(self):
          return f'{self.user.nome} inscrito em {self.event.title}'