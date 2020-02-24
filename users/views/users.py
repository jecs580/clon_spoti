"""Vistas de User."""

# Django REST Framework
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

# Model
from users.models import User

# Serializers
from users.serializers import (
    UserModelSerializer,
    UserSignupSerializer,
    AccountVerificationSerializer,
    UserLoginSerializer)

# Permissions
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
from users.permissions import IsAccountOwner
class UserViewSet(
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    """Vistas de Usuario."""
    
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    lookup_field='username'

    def get_permissions(self):
        """Asigna permisos en función de la acción."""
        if self.action in ['signup', 'login', 'verify']:
            permissions=[AllowAny] # No colocamos comillas por que es una clase que se coloca.
        elif self.action in ['retrieve', 'update','partial_update']:
            permissions=[IsAuthenticated, IsAccountOwner] # Permitira la vista solo si esta autenticado y el usuario que quiere recuperar es el propietario
        else:
            permissions=[IsAuthenticated]
        return [permission() for permission in permissions]

    @action(detail=False,methods=['post'])
    def signup(self,request):
        """Registro de Usuarios."""
        serializer=UserSignupSerializer(data=request.data)  # Restauramos los datos del request a un diccionario
        serializer.is_valid(raise_exception=True)  # Validamos los datos
        user=serializer.save()  # Creacion un usuario y lo retornamos
        data=UserModelSerializer(user).data # Serializamos los datos
        return Response(data,status=status.HTTP_201_CREATED)  # Enviamos los datos serializados como respuesta.

    @action(detail=False, methods=['post'])
    def verify(self, request):
        """Verica que el correo registrado sea del usuario"""
        serializer = AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data={'mensaje':'¡Felicidades, ahora puedes usar la API!'}
        return Response(data,status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['post'])
    def login(self, request):
        """Inicio de sesion de Usuarios."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user,token = serializer.save()
        data={
            'user':UserModelSerializer(user).data,
            'access_token':token
        }
        return Response(data, status=status.HTTP_200_OK)