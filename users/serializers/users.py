"""Serializador de Usuarios."""

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token
# Django
from django.contrib.auth import authenticate, password_validation
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

# Model
from users.models import User

# Utilities
from django.utils import timezone
from datetime import timedelta
import jwt


class UserModelSerializer(serializers.ModelSerializer):
    """Serializador del Modelo de Usuarios."""

    class Meta:
        """Clase Meta."""
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )


class UserSignupSerializer(serializers.Serializer):
    """Serializador de registro de Usuarios."""
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())])
    # password
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)
    # Name
    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)

    def validate(self, data):
        """Verifica que coincidan los passwords"""
        password = data['password']
        password_confirmation = data['password_confirmation']
        if password != password_confirmation:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        password_validation.validate_password(password)
        return data

    def create(self, data):
        """Creacion de un nuevo usuario y un perfil"""
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        self.send_confirmation_email(user)
        return user

    def send_confirmation_email(self, user):
        """Envia un enlace de verificación de cuenta a usuario dado
            Enviando un email al usuario para verificar la cuenta
        """
        verification_token = self.gen_verification_token(user)
        subject = 'Bienvenido @{}! Verifica tu cuenta para empezar a usar Clon Spoti'.format(
            user.username)
        from_email = 'Clon Spoti <noreply@jorgecallisay.me>'
        content = render_to_string(
            'emails/users/account_verification.html',
            {'token': verification_token, 'user': user}
        )

        msg = EmailMultiAlternatives(
            subject,
            content,
            from_email,
            [user.email]  # Lista de direcciones de correos a enviar
        )
        msg.attach_alternative(
            content,
            "text/html")
        msg.send()
        # Usaremos los JWT para enviar la informacion del usuario sin
        # necesidad de guardarlo en la base de datos.

    def gen_verification_token(self, user):
        """Crea un token JWT que el usuario pueda usar para
        verificar su cuenta"""
        # El self se utiliza para que la funcion pueda usar los
        # atributos de la clase.
        exp_date = timezone.now()+timedelta(days=3)
        payload = {
            'user': user.username,
            'exp': int(exp_date.timestamp()),
            'type': 'email_confirmation'
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        return token.decode()


class AccountVerificationSerializer(serializers.Serializer):
    """Serializador para verificar la cuenta."""

    token = serializers.CharField()

    def validate_token(self, data):
        """Verificamos que el token sea valido"""

        try:
            payload = jwt.decode(data, settings.SECRET_KEY,
                                 algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise serializers.ValidationError(
                'El enlace de verificacion ha expirado')
        except jwt.PyJWTError:
            raise serializers.ValidationError('Token invalido')
        if payload['type'] != 'email_confirmation':
            raise serializers.ValidationError('Token invalido')

        self.context['payload'] = payload
        return data

    def save(self):
        """Actualizamos el estado de verifcado del usuario

        Sobre-escribimos el metodo save en lugar de create o update
        por que no devolveremos nada
        """
        payload = self.context['payload']
        user = User.objects.get(username=payload['user'])
        user.is_verified = True
        user.save()


class UserLoginSerializer(serializers.Serializer):
    """Serializador para inicio de sesion."""

    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        """Verifica las credenciales."""
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Credenciales Invalidas')
        if not user.is_verified:
            raise serializers.ValidationError('La cuenta no esta verificada')
        self.context['user'] = user
        return data

    def create(self, data):
        """Recupera o crea un nuevo token."""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key
