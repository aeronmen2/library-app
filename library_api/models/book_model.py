from django.db import models
from .author_model import Author
from .publisher_model import Publisher
from .category_model import Category

class Book(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    page_count = models.IntegerField()
    language = models.CharField(max_length=50)
    format = models.CharField(max_length=50)
    authors = models.ManyToManyField(Author, related_name='books')    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='books')
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True, related_name='books')
