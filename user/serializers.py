import re

from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.db import DatabaseError
from rest_framework import serializers
from rest_framework.serializers import CharField,ValidationError,EmailField,ImageField,IntegerField,DateTimeField

from myapp.models import BlogUser


class RegisterSerializer(serializers.Serializer):
    username = CharField()
    password = CharField()
    email = EmailField()
    nickname = CharField()
    create_time = DateTimeField()
    last_mod_time = DateTimeField()
    qq = CharField()
    mobile = CharField()

    def save(self,**kwargs):
        email = self.validated_data['email']
        password = self.validated_data['password']
        username = self.validated_data['username']
        nickname = self.validated_data['nickname']
        create_time = self.validated_data['create_time']
        last_mod_time = self.validated_data['last_mod_time']
        qq = self.validated_data['qq']
        mobile = self.validated_data['mobile']

        try:
            user = BlogUser.objects.create(username=username,
                                           password=password,
                                           email=email,
                                           nickname=nickname,
                                           create_time=create_time,
                                           last_mod_time=last_mod_time,
                                           qq=qq,
                                           mobile=mobile)
            user.save()
            return True
        except DatabaseError:
            return False

    @staticmethod
    def validate_username(value):
        if re.match(r'^[a-zA-Z0-9\-]{4,20}$',value) is None:
            raise ValidationError(
                'Username can only contain letters,numbers,-,_ and no shorter than 4 and no longer than 20'
            )
        try:
            BlogUser.objects.get(username=value)
            raise ValidationError('Username exist')
        except ObjectDoesNotExist:
            pass
        return value

    @staticmethod
    def validate_password(value):
        if re.match(r'^[a-zA-Z0-9\-.]{8,30}$',value) is None:
            raise  ValidationError(
                'Password can only contains letters,numbers,-,_,. and no shorter than 8 and no longer than 30'
            )
        return value

    @staticmethod
    def validate_email(value):
        if len(value)>128:
            raise ValidationError('email address is too long')
        try:
            BlogUser.objects.get(email=value)
            raise ValidationError('Email address has been registered')
        except ObjectDoesNotExist:
            pass
        return value

    @staticmethod
    def validate_mobile(value):
        if len(value) != 11:
            raise ValidationError('The value is not a phone number')
        try:
            BlogUser.objects.get(mobile=value)
            raise ValidationError('The phone number has been registered')
        except ObjectDoesNotExist:
            pass
        return value



class LoginSerializer(serializers.Serializer):
    username = CharField()
    password = CharField()

    @staticmethod
    def validata_username(value):
        if re.match(r'^[a-zA-Z0-9\-_]{4,20}$',value) is None:
            raise ValidationError(
                'Username can only contain letters,numbers,-,_ and no shorter than 4 and no longer than 20'
            )
        return value

    @staticmethod
    def validate_password(value):
        if re.match(r'^[a-zA-Z0-9\-.]{8,30}$', value) is None:
            raise ValidationError(
                'Password can only contains letters,numbers,-,_,. and no shorter than 8 and no longer than 30'
            )
        return value

    def login(self,request):
        user = auth.authenticate(username=self.validated_data['username'],
                                 password=self.validated_data['password'])

        if user:
            if request:
                auth.login(request,user)
            return user


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = BlogUser
        fields = ('username','nickname','qq','mobile','is_superuser')