from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .models import *
# Create your views here.
def Login(req):
    if (req.method == 'GET'):
        return render(req,'myusers/login.html')
    else:
        u= Myuser.objects.filter(username=req.POST['username'],Password=req.POST['password'])
        if(len(u)>0 ):
            return HttpResponseRedirect('/')
        else:
            context={}
            context['msg']='ivalid user name or password'
            return render(req, 'myusers/login.html',context)
def reg(req):
    if(req.method=='GET'):
        return render(req,'myusers/register.html')
    else:
        print(req.POST)
        Myuser.objects.create(name=req.POST['name'],Password=req.POST['password'],username=req.POST['username'],age=req.POST['age'])
        return HttpResponseRedirect('/Users/Login')
def Logout(req):
    return HttpResponse('Logout')