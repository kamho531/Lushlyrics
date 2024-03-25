from django.urls import path
from . import views

urlpatterns = [
    path('', views.userlogin, name='userlogin'),
    path('register/', views.register, name='register'),
    path('logout/', views.userlogout, name='userlogout'),

]