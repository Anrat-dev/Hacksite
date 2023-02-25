from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import datetime
from django.db.models import Avg, Count, Min, Sum
from .models import Meal, GameType, Calories, UserMeals, UserPoints, UserCalories, UserGameType

# Create your views here.

def home_page(request):
    user_points = UserPoints.objects.filter(player=request.user).aggregate(Sum('points'))
    user_meals = UserMeals.objects.filter(player=request.user, meal_date=datetime.date.today()).count()
    user_meals_all = UserMeals.objects.filter(player=request.user).count()
    user_calories = UserCalories.objects.filter(player=request.user, meal_date=datetime.date.today()).aggregate(Sum('calories'))
    acct = UserGameType.objects.get(player=request.user)
    acct_type = acct.game_type

    return render(request, 'eatdapoints/home_page.html', {'user_points': user_points, 'user_meals': user_meals, 'user_meals_all': user_meals_all, 'user_calories': user_calories, 'acct_type': acct_type})


def meal_list(request):
    user_meal_list = UserMeals.objects.filter(player=request.user).order_by('-meal_date')
    user_meals_count = UserMeals.objects.filter(player=request.user).count()

    return render(request, 'eatdapoints/meal_list.html', {'user_meal_list': user_meal_list, 'user_meals_count': user_meals_count})


def point_list(request):
    user_points_list = UserPoints.objects.filter(player=request.user).order_by('-meal_date')
    user_points_tot = UserPoints.objects.filter(player=request.user).aggregate(Sum('points'))
