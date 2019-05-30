from django.urls import path
from django.urls import include
from django.contrib import admin
from admin import views

urlpatterns = [
    path('',views.admin,name='admin'),
    path('login/',views.admin_login,name='admin_login'),
    path('register/',views.admin_register,name='admin_register'),
    path('auth/',include("user.urls"))
]