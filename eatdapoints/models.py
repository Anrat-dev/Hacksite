from django.db import models
from django.contrib.auth.models import User
import datetime
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Meal(models.Model):
    meal_type = models.CharField(max_length=200, unique=True)
    meal_description = models.TextField()
    points = models.IntegerField(default=20, blank=False, null=False)

    def __str__(self):
        return self.meal_type


class GameType(models.Model):
    game_type = models.CharField(max_length=50, unique=True)
    game_description = models.TextField()

    def __str__(self):
        return self.game_type

class UserMeals(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE) 
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    meal_date = models.DateField(default=datetime.date.today)
    meal_time = models.TimeField(default=timezone.now)

    def __str__(self):
        return (self.player + self.meal + str(self.meal_date))

class UserPoints(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE) 
    meal_type = models.ForeignKey(Meal, on_delete=models.CASCADE)
    points = models.IntegerField()
    meal_date = models.DateField(default=datetime.date.today)
    meal_time = models.TimeField(default=timezone.now)

    def __str__(self):
        return (self.player + self.meal + str(self.meal_date))