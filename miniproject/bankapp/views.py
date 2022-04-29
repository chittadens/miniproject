from django.shortcuts import render


def index1(request):
     return render(request, 'login.html')


def index2(request):
    return render(request, 'admin.html')


def index3(request):
     return render(request, 'target.html')
