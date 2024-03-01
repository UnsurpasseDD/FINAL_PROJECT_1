from django.urls import path, include
from django.contrib import admin
from .views import *

urlpatterns = [
    path('news/', NewsList.as_view(), name='post_list')
]