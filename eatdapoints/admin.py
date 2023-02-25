from django.contrib import admin

# Register your models here.

from .models import Meal, Calories, GameType, UserGameType, UserMeals ,UserCalories, UserPoints

admin.site.register(Meal)
admin.site.register(Calories)
admin.site.register(GameType)
admin.site.register(UserGameType)
admin.site.register(UserMeals)
admin.site.register(UserCalories)
admin.site.register(UserPoints)