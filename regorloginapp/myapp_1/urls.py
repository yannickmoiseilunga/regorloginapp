from django.shortcuts import render
from django.urls import include, path
from . import views
#from .myapp_1 import views

from .models import Regbase


app_name = 'myapp_1'


urlpatterns = [

    path('', views.index, name = 'index'),
#    path('<int:Addnum_id>/', views.student, name = 'student'),
    path('signup/', views.signup, name = 'signup'),
    path('login/', views.login, name = 'login'),

    path('login/result/', views.result, name = 'login/result'),
    path('signup/result/', views.result, name = 'signup/result'),
#
]
