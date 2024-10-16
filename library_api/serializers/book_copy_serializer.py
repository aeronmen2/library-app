from rest_framework import serializers
from ..models import BookCopy
from .book_serializer import BookSerializer

class BookCopySerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = BookCopy
        fields = '__all__'
