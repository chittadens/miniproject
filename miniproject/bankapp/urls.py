from django.urls import path
from .import views

urlpatterns = [
    path('index1/', views.index1,name="adam"),
    path('index2/', views.index2,name="emy"),
    path('index3/', views.index3),
    path('index4/', views.index4),
    path('index5/', views.index5,name="jack"),

]
