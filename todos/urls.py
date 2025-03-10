from django.contrib import admin
from django.urls import path
from todos import views

# dev_1
urlpatterns = [
    path("", views.home,name="home"),
]
