from django.contrib import admin
from django.urls import path, include
from home import views


urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.UserLogin, name='login'),
    path('logout', views.UserLogout, name='logout'),

]
