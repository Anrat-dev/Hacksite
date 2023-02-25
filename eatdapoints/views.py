from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import datetime
from django.db.models import Avg, Count, Min, Sum
from .models import Meal, GameType, Calories, UserMeals, UserPoints, UserCalories, UserGameType

def home(request):
  template = loader.get_template('homepage.html')
  return HttpResponse(template.render())
