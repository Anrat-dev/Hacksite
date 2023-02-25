from django.urls import path
from eatdapoints import views

urlpatterns = [
    path("", views.home_page, name="home"),
]