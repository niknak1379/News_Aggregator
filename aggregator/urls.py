from djangoProject.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from aggregator.views import *

urlpatterns = [
    path('', ArticleList.as_view(), name='article_list'),
    path('sort/', views.sort, name='sort'),
    path('filter/', views.custom_filter, name='filter'),
    path('csrf/', views.csrf),
    path('ping/', views.ping),

]