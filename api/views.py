from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Point de terminaison de l'API qui permet aux utilisateurs d'être affichés ou modifiés.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    Point de terminaison de l'API qui permet d'afficher ou de modifier les groupes.
    """
    
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]