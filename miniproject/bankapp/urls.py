from django.urls import path
from .import views

urlpatterns = [
    path('', views.home,name="home"),
    path('login/', views.login,name="login"),
    path('admin/', views.admin,name="admin"),
    path('target/', views.target,name="target"),
    path('index4/', views.index4),
    path('manager/', views.manager,name="manager"),
    path('customers/', views.customers,name="customer"),
    path('index7/', views.index7,name="tom"),
    path('table/', views.table),

]
