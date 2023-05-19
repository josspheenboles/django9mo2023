from django.contrib import admin
from django.urls import path
from myusers.views import *
urlpatterns = [
    path('Login',Login,name='Login'),
    path('Logout',Logout,name='Logout'),
    path('registration',reg,name='regsitration')
]