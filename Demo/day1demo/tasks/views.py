from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from .models import *
from .forms import TaskForm,TaskformModel
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views import View
from django.views.generic import CreateView

class TaskGErtnic(CreateView):
    model = Task
    fields='__all__'





# Create your views here.
@require_http_methods(['POST','GET'])
def taskadd(req):
    #return HttpResponse('Task add form will be load')
    #return  HttpResponseRedirect('/')
    context = {}
    myform=TaskformModel()
    # select all catagories
    context['catagories'] = Catagory.objects.all()

    if(req.method=='GET'):
        context['myform']=myform
        return render(req,'tasks/add.html',context)
    else:
        #insert task in model task
        myform=TaskForm(req.POST)
        if(myform.is_valid()):
            #create object from task mode
            myform.save()
        #t=Task(name=nameinpu)
        #t.catagoryobj=Catagory.objects.get(id=catagoryid)
        #save object
        #t.save()
            return HttpResponseRedirect('/')

class TaskADD(View):
    def get(self,req):
        context={}
        myform=TaskForm
        context['myform'] = myform
        return render(req, 'tasks/add.html', context)
    def post(self,req):
        # insert task in model task
        myform = TaskForm(req.POST)
        if (myform.is_valid()):
            # create object from task mode
            myform.save()
            # t=Task(name=nameinpu)
            # t.catagoryobj=Catagory.objects.get(id=catagoryid)
            # save object
            # t.save()
            return HttpResponseRedirect('/')



def list(request):
    '''
    print(type(request))
    resp=HttpResponse('<h1>List</h1>')
    resp['content-type']='text/plain'
    resp.write('View')
    resp.set_cookie('date','18-5-2023')
    #return HttpResponse('<h1>list view response</h1>')
    resp=JsonResponse({'name':'aya'})
    context={}
    context['pagename']='Tasks\nList'
    context['tasks']=['task1','task2','task3']
    '''
    context={}

    #get all task from model

    context['tasks']=Task.objects.all()
    return  render(request,'tasks/list.html',context)



def taskupdate(req,ID):
    contex={}
    contex['catagories']=Catagory.objects.all()
    contex['task']=Task.objects.get(id=ID)
    if(req.method=='GET'):
        return render(req,'tasks/update.html',contex)
    else:
        nameinpu=req.POST['name']
        catagoryobjinput = Catagory.objects.get(id=req.POST['catagory'])
        Task.objects.filter(id=ID).update(name=nameinpu,catagoryobj=catagoryobjinput)
        return HttpResponseRedirect('/')
def taskdelete(req,ID):
    Task.objects.filter(id=ID).delete()
    return  HttpResponseRedirect('/')