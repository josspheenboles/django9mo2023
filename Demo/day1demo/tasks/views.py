from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from .models import *

# Create your views here.
def taskadd(req):
    #return HttpResponse('Task add form will be load')
    #return  HttpResponseRedirect('/')
    context = {}
    # select all catagories
    context['catagories'] = Catagory.objects.all()

    if(req.method=='GET'):
        return render(req,'tasks/add.html',context)
    else:
        #insert task in model task
        #get data
        nameinpu=req.POST['name']
        catagoryid=req.POST['catagory']
        #create object from task mode
        Task.objects.create(name=nameinpu,catagoryobj=  Catagory.objects.get(id=catagoryid))
        #t=Task(name=nameinpu)
        #t.catagoryobj=Catagory.objects.get(id=catagoryid)
        #save object
        #t.save()
        return HttpResponseRedirect('/')



#view method httprequest as argument & return HttpResponse
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