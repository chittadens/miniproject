from django.shortcuts import redirect, render
from . models import *


def home(request):
     return render(request, 'home.html')


def home1(request):
     return render(request, 'home1.html')


def login(request):
     return render(request, 'login.html')


def stafflogin(request):
     return render(request, 'stafflogin.html')


def managerlogin(request):
     return render(request, 'managerlogin.html')


def asstmanagerlogin(request):
     return render(request, 'asstmanagerlogin.html')


def asstmanagerprofiles(request):
     return render(request, 'asstmanagerprofiles.html')


def admin(request):
    return render(request, 'admin.html')


def forgot(request):
    return render(request, 'forgot.html')


def attendance(request):
    return render(request, 'attendance.html')


def registration(request):
    return render(request, 'registration.html')


def targets(request):
     return render(request, 'targets.html')


def staffs(request):
     return render(request, 'staffs.html')


def edit(request):
     return render(request, 'edit.html')


def managerprofiles(request):
     return render(request, 'managerprofiles.html')


def adminclerkprofile(request):
     return render(request, 'adminclerkprofile.html')


def staffprofile(request):
     return render(request, 'staffprofile.html')

def clerkprofile(request):
     return render(request, 'clerkprofile.html')


def adminmanager(request):
     return render(request, 'adminmanager.html')


def adasstmaprofile(request):
     return render(request, 'ad asst ma profile.html')


def index4(request):
     return render(request,'dupli.html')


def managerhome(request):
     return render(request,'managerhome.html') 


def managerstaff(request):
     return render(request,'managerstaff.html') 


def staffhome(request):
     return render(request,'staffhome.html') 


def customers(request):
     return render(request,'customers.html')


def schemes(request):
     return render(request,'schemes.html')


def reports(request):
     return render(request,'reports.html')


def reset(request):
     return render(request,'reset.html')


def notifications(request):
     return render(request,'notifications.html')


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


def maamprofile(request):
     if 'xyz' in request.session:
          current_user=request.session['xyz']
          profile_details=Registration.objects.get(id=current_user)
          return render(request, 'maamprofile.html',{'profile':profile_details})
     return render(request,'mammlogin.html',{"message":"login your profile"}) 


def maamproduct(request):
     if request.method=='POST':
          productname=request.POST['productname']
          price=request.POST['price']
          description=request.POST['description']
          images=request.FILES['images']
     return render(request,'maamproduct.html')    

 
         
