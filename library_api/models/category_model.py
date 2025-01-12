from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name