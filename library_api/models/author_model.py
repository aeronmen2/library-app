from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=50)

    def __str__(self):
        return self.name