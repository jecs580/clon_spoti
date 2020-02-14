"""Vistas de User."""

# Django REST Framework
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

# Model
from users.models import User

# Serializers
from users.serializers import UserModelSerializer, UserSignupSerializer

    
class UserViewSet(
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    """Vistas de Usuario."""

    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    @action(detail=False,methods=['post'])
    def signup(self,request):
        """Registro de Usuarios."""
        serializer=UserSignupSerializer(data=request.data)  # Restauramos los datos del request a un diccionario
        serializer.is_valid(raise_exception=True)  # Validamos los datos
        user=serializer.save()  # Creacion un usuario y lo retornamos
        data=UserModelSerializer(user).data # Serializamos los datos
        return Response(data,status=status.HTTP_201_CREATED)  # Enviamos los datos serializados como respuesta.