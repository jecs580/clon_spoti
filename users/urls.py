"""Urls de Users."""

# Django
from django.urls import path, include

# Views
from .views import users as user_views

# Django REST Framework
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(
    r'users',
    user_views.UserViewSet,
    basename='users'
)

urlpatterns = [
    path('', include(router.urls))
]