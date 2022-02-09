from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [

    path('', Home, name='Home'),
    path('reviews', reviews, name='reviews'),
]
