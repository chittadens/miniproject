from django.urls import path
from .import views

urlpatterns = [

    path('regist/',views.regist),
    path('index/',views.regist),

]