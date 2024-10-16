from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    website = models.URLField()
    contact_email = models.EmailField()
    description = models.TextField()
