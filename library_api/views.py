from rest_framework import viewsets, filters
from .models import Author, Publisher, Category, Book, BookCopy, Loan, Comment, Rating
from .serializers import AuthorSerializer, PublisherSerializer, CategorySerializer, BookSerializer, BookCopySerializer, LoanSerializer, CommentSerializer, RatingSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .permissions import IsReadOnly, IsAdminUser


class AuthorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class PublisherViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

class BookCopyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = BookCopy.objects.all()
    serializer_class = BookCopySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['book__title']


class LoanViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]   
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    filter_backends = [filters.SearchFilter]


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [filters.SearchFilter]

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    filter_backends = [filters.SearchFilter]

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated, IsReadOnly|IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]