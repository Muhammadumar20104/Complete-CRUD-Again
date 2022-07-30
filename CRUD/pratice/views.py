from django.shortcuts import render
from django.http import HttpResponse
from . models import Details
from . forms import *
# Create your views here.
def create(request):
    frm = Df
    if request.method == 'POST':
        frm= Df(request.POST)
        if frm.is_valid():
            frm.save()
            frm = Df()
    else:
        frm = Df()
    data = Details.objects.all()
    return render(request,"Form.html",{'Form':frm,'data':data})
def read(request):
    var=Details.objects.all()
    return render(request,'Read.html',{'data':var})
def update(request,data):
    print(data)
    a=Details.objects.get(id =data)
    va=Df(request.POST or None,instance=a)
    if va.is_valid():
        va.save()
        va=Df()
    DATA=Details.objects.all()    
    return  render(request,'update.html',{'va':va,"data":DATA})
def delete(request,data):
    a=Details.objects.get(id =data)
    va=Df(request.POST or None,instance=a)
    if va.is_valid():
        a.delete()
        va=Df()
    DATA=Details.objects.all()    
    return  render(request,'delete.html',{'va':va,"data":DATA})
