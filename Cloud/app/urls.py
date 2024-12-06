from django.urls import path
from . import views
urlpatterns=[
    path('',views.home),
    path('logout',views.e_logout),
    path('login',views.e_login),
    path('register',views.register),
    path('view/',views.view),
    path('add/',views.add),
]