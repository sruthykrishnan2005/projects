
from django.contrib import admin
from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path('', views.home),         # Home page
    path('about/', views.about), # About page
    path('contact/', views.contact), # Contact Us page
]
