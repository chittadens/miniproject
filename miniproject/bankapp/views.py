from django.shortcuts import render
from . models import *


def home(request):
     return render(request, 'home.html')


def login(request):
     return render(request, 'login.html')


def admin(request):
    return render(request, 'admin.html')


def target(request):
     return render(request, 'target.html')


def index4(request):
     return render(request,'dupli.html')


def manager(request):
     return render(request,'manager.html') 


def customers(request):
     return render(request,'customers.html')


def index7(request):
     if request.method=='POST':
          name=request.POST['username']
          password=request.POST['password']
          email=request.POST['email']
          age=request.POST['age']
          details=Registration(username=name,password=password,email=email,age=age)
          details.save()
     return render(request,'regist.html')


def  table(request):
     infodetails=Registration.objects.all()
     return render(request,'table.html',{'info':infodetails})


         
