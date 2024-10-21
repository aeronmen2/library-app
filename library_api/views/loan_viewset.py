from rest_framework import viewsets, filters
from ..models import Loan
from ..serializers import LoanSerializer
from rest_framework.permissions import IsAuthenticated

class LoanViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    filter_backends = [filters.SearchFilter]
