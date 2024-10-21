from rest_framework import viewsets, filters
from ..models import Publisher
from ..serializers import PublisherSerializer
from rest_framework.permissions import IsAuthenticated

class PublisherViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
