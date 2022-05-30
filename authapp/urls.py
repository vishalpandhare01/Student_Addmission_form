from django.contrib import admin
from django.urls import path ,include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('reg/',views.reg,name="reg"),
    path('login1/',views.login1,name="login1"),
    path('logout1/',views.logout1,name="logout1"),
    path('main/',views.main,name="main"),
]