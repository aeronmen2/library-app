from rest_framework import viewsets, filters
from ..models import BookCopy
from ..serializers import BookCopySerializer
from rest_framework.permissions import IsAuthenticated

class BookCopyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = BookCopy.objects.all()
    serializer_class = BookCopySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['book__title']
