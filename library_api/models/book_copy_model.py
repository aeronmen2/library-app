from django.db import models
from .book_model import Book

class BookCopy(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='copies')
    condition = models.CharField(max_length=50)
    acquisition_date = models.DateField()
    location = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)
