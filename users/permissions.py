"""Permisos de Usuario"""

# Django REST Framework
from rest_framework.permissions import BasePermission


class IsAccountOwner(BasePermission):
    """Permite acceso solo a los objetos propiedad del usuario solicitante"""

    def has_object_permission(self, request, view, obj):
        """Comprueba que obj y usuario son iguales"""
        return request.user == obj
