from rest_framework import viewsets, filters
from django.contrib.auth.models import User
from ..serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from ..permissions import IsReadOnly, IsAdminUser

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated, IsReadOnly | IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
