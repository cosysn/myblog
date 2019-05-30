from django.urls import path
from user.views import AuthAPI,RegisterAPI

urlpatterns = [
    path('Login',AuthAPI.as_view(),name='user_login'),
    path('Reginster',RegisterAPI.as_view(),name='user_register')
]