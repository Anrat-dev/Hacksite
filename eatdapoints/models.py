from django.db import models

# Create your models here.
from django.conf import settings
from django.utils import timezone


class Meal(models.Model):
    meal_type = models.CharField(max_length=200, unique=True)
    meal_description = models.TextField()

    def __str__(self):
        return self.meal_type

