from django.db import models
from django.contrib.auth.models import User
from .book import Book

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='ratings')
    score = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(blank=True)
    rating_date = models.DateTimeField(auto_now_add=True)
    is_recommended = models.BooleanField(default=False)
    title = models.CharField(max_length=100, blank=True)
