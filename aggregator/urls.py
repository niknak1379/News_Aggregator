from djangoProject.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('sort/', views.sort, name='sort'),
    path('filter/', views.custom_filter, name='filter')
]