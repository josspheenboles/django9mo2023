from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .forms import *
from django.contrib.auth.models import User
from  django.contrib.auth import login as authlogin,authenticate
# Create your views here.
def Login(req):
    context={}
    form=Mylogin()
    context['form']=form
    if(req.method=='POST'):
        form=Mylogin(req.POST)
        if(form.is_valid()):
            u=Myuser.objects.filter(username=form.cleaned_data['username'],Password=form.cleaned_data['password'])
            authuser=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if(len(u)>0 and authuser is not None):
                req.session['username']=u[0].username
                #autologin admin pane
                authlogin(req,authuser)

                return  HttpResponseRedirect('/')
    return render(req, 'myusers/login.html',context)
def reg(req):
    context={}
    form=Myreg()
    context['form']=form
    if(req.method=='POST'):
        form = Myreg(req.POST)
        if(form.is_valid()):
            form.save()
            User.objects.create_superuser(username=req.POST['username'],password=req.POST['Password'],email=req.POST['email'],is_active=True)
    return render(req,'myusers/register.html',context)
def Logout(req):
    req.session.clear()
    return HttpResponse('/')