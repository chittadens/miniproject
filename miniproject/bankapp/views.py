from django.shortcuts import render


def index1(request):
     return render(request, 'login.html')


def index2(request):
    return render(request, 'admin.html')


def index3(request):
     return render(request, 'target.html')


def index4(request):
     return render(request,'dupli.html')


def index5(request):
     return render(request,'manager.html') 


def index6(request):
     return render(request,'adm.html')


         
