from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=30)
    category = models.CharField(max_length=40)
    time = models.TimeField()

    def __str__(self):
        return self.title