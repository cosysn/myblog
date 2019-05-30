from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader



def admin(request):
    return HttpResponse("world. You're at the admin index")


def admin_login(request):
    template = loader.get_template('admin/login.html')
    content = {}
    return HttpResponse(template.render(content,request))

def admin_register(request):
    template = loader.get_template('admin/register.html')
    content = {}
    return HttpResponse(template.render(content,request))
