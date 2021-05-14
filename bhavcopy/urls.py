from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
  
    path('bhavcopy/', views.get_bhavcopy, name='bhavcopy'),
  

] 