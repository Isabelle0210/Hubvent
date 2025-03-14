
from rest_framework import permissions


class IsOwnerOrAdmin (permissions.BasePermission):
     """Permite que os usuários editem apenas seus próprios eventos."""
     
     def has_permission(self, request, view):
          #qualquer usuario autenticado pode criar um evento
          if request.method in permissions.SAFE_METHODS or request.method == 'POST':
               return request.user and request.user.is_authenticated
          return True
     
     
     def has_object_permission(self, request, view, obj):
          #apenas o dono do evento ou um admin pode editar um evento
          return request.user.is_staff or obj.created_by == request.user