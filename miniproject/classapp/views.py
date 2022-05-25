from django.http import JsonResponse
from django.shortcuts import render

from classapp.models import Login

def regist(request):
    username=request.POST['username']
    password=request.POST['password']
    email=request.POST['email']
    age=request.POST['age']
    login_details=Login(username=username,password=password,email=email,age=age)
    login_details.save()
    return JsonResponse({'message': "username password enter"})
    


def index(request):
    return render(request,'regist.html')
