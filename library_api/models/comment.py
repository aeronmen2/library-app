from django.db import models
from django.contrib.auth.models import User
from .book import Book

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    is_visible = models.BooleanField(default=True)
    is_moderated = models.BooleanField(default=False)
