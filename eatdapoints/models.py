from django.db import models
from django.contrib.auth.models import User
import datetime
from django.conf import settings
from django.utils import timezone

# Create your models here.
GAME_CHOICES =(
    ("MealPlan", "MealPlan"),
    ("CalorieCounting", "CalorieCounting")
)

class Meal(models.Model):
    meal_type = models.CharField(max_length=200, unique=True)
    meal_description = models.TextField()
    points = models.IntegerField(default=20, blank=False, null=False)

    def __str__(self):
        return self.meal_type

class Calories(models.Model):
    calorie_amt = models.IntegerField(unique=True)
    points = models.IntegerField(default=20, blank=False, null=False)

    def __str__(self):
        return str(self.calorie_amt)

class GameType(models.Model):
    game_type = models.CharField(max_length=50, unique=True)
    game_description = models.TextField()

    def __str__(self):
        return self.game_type

class UserGameType(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    game_type = models.CharField(max_length=25, choices=GAME_CHOICES, default="MealPlan")

    def __str__(self):
        return (self.player.username + '_' + self.game_type)

class UserMeals(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE) 
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    meal_date = models.DateField(default=datetime.date.today)
    meal_time = models.TimeField(default=timezone.now)

    def __str__(self):
        return (self.player.username + '_' + self.meal.meal_type + '_' + str(self.meal_date))

class UserCalories(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE) 
    calories = models.ForeignKey(Calories, on_delete=models.CASCADE)
    meal_date = models.DateField(default=datetime.date.today)
    meal_time = models.TimeField(default=timezone.now)

    def __str__(self):
        return (self.player.username + '_' + str(self.calories.calorie_amt) + '_' + str(self.meal_date))

class UserPoints(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE) 
    meal_type = models.ForeignKey(Meal, on_delete=models.CASCADE)
    points = models.IntegerField()
    meal_date = models.DateField(default=datetime.date.today)
    meal_time = models.TimeField(default=timezone.now)

    def calculate_points(self):
        self.points = self.meal_type.points
        self.save()

    def __str__(self):
        return (self.player.username + '_' + str(self.points) + '_' + str(self.meal_date))

class UserMealPlan(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    meal_type = models.ManyToManyField(Meal)

    def __str__(self):
        return (self.player.username)

class UserCalorieCount(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    calorie_count = models.ForeignKey(Calories, on_delete=models.CASCADE)
    
    def __str__(self):
        return (self.player.username)