from django.shortcuts import redirect, render
from . models import *


def home(request):
     return render(request, 'home.html')


def login(request):
     return render(request, 'login.html')


def admin(request):
    return render(request, 'admin.html')


def forgot(request):
    return render(request, 'forgot.html')


def registration(request):
    return render(request, 'registration.html')


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
          return redirect("table")
     return render(request,'regist.html')


def  table(request):
     infodetails=Registration.objects.all()
     return render(request,'table.html',{'info':infodetails})


def delete(request,id):
     Registration.objects.get(id=id).delete()
     return redirect("table")


def update(request,id):
     updatedata=''
     if request.method=='POST':
         name=request.POST['username']
         password=request.POST['password']
         email=request.POST['email']
         age=request.POST['age'] 
         Registration.objects.filter(id=id).update(username=name,password=password,email=email,age=age)
         return redirect("table")
     else:
          updatedata=Registration.objects.get(id=id)
     return render(request,'form.html',{'update':updatedata}) 


def mammlogin(request):
     if request.method=='POST':
          name=request.POST['username']
          password=request.POST['password']
          try:
               current_user=Registration.objects.get(username=name,password=password)
               request.session['xyz']=current_user.id
               return redirect("table")
          except Registration.DoesNotExist:
               return render(request,'mammlogin.html',{"message":"username password wrong"})
     return render(request,'mammlogin.html') 


def logout(request):
     request.session.flush()
     return redirect("maamlogin")
        

 
         
