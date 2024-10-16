from rest_framework import serializers
from ..models import Book
from .author_serializer import AuthorSerializer
from .category_serializer import CategorySerializer
from .publisher_serializer import PublisherSerializer

class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    publisher = PublisherSerializer(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
