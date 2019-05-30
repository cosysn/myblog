from django.shortcuts import render
from user.serializers import LoginSerializer,RegisterSerializer,UserProfileSerializers

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.views import Response
from myapp.models import BlogUser
from utils.response import res_format,Message
from django.contrib import auth
# Create your views here.


class RegisterAPI(APIView):
    def post(self,request,**kwargs):
        register = RegisterSerializer(data=request.data)
        if register.is_valid():
            if register.save():
                return Response(res_format("Register Success"))
            else:
                return Response(res_format('System error',status=Message.ERROR))
        else:
            return Response(res_format(register.errors,Message.ERROR))

class AuthAPI(APIView):
    def get(self,request,**kwargs):
        if request.user and request.user.is_authenticated:
            return Response(res_format(str(request.user),status=Message.SUCCESS))
        return Response(res_format('Login required',status=Message.ERROR))

    def post(self,request,**kwargs):
        serializers = LoginSerializer(data=request.data)
        if serializers.is_valid():
            user = serializers.login(request)
            if user:
                return Response(res_format(UserProfileSerializers(user).data,status=Message.SUCCESS),
                                status=status.HTTP_200_OK)
            else:
                return Response(res_format('Incorrect username or password',status=Message.ERROR))
        print('serializers.errors')
        return Response(res_format(serializers.errors,Message.ERROR))

    def delete(self,request,**kwargs):
        print('delete')
        auth.logout(request)
        return Response(res_format('Logout Success',status=Message.SUCCESS))
