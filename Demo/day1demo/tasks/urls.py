from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',list,name='TasksList'),
    path('Tasks/Add',taskadd,name='TasksAdd'),
    path('Tasks/Update/<int:ID>',taskupdate,name='TasksUpdate'),
    path('Tasks/Delete/<int:ID>',taskdelete,name='TasksDelete'),

]