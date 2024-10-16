from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, PublisherViewSet, CategoryViewSet, BookViewSet, BookCopyViewSet, LoanViewSet, CommentViewSet, RatingViewSet, UserViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'publishers', PublisherViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'books', BookViewSet)
router.register(r'bookcopies', BookCopyViewSet)
router.register(r'loans', LoanViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'ratings', RatingViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]