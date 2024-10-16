from rest_framework import serializers
from ..models import Loan
from .book_copy_serializer import BookCopySerializer

class LoanSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    book_copy = BookCopySerializer(read_only=True)

    class Meta:
        model = Loan
        fields = '__all__'
