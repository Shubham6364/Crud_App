from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
# Create your views here.
def index(request):
    result = CrudApp.objects.all()
    context = {
        'result':result,
    }   
    return render(request,'index.html',context)


def add(request):
    if request.method == 'POST':
        Name = request.POST.get('fname')
        Email = request.POST.get('email')
        Address = request.POST.get('address')
        Phone = request.POST.get('number')
        
        result = CrudApp(Name=Name, Email=Email, Address=Address,Phone=Phone)
        result.save()
        
        return redirect('index')
        
    return render(request,'index.html')

def edit(request):
    result = CrudApp.objects.all()
    
    context={
        'result':result,
    }
    return render(request,'index.html')


def update(request,id):
    if request.method == 'POST':
        Name = request.POST.get('fname')
        Email = request.POST.get('email')
        Address = request.POST.get('address')
        Phone = request.POST.get('number')  
        
        result = CrudApp(id=id,Name=Name,Email=Email, Address=Address,Phone=Phone)
        result.save()
        
        return redirect('index')
    return render(request,'index.html')


def delete(request,id):
    result = CrudApp.objects.filter(id=id)
    result.delete()
    
    context = {
        'result':result,
    }
    return redirect('index')
    return render(request,'index.html',context)