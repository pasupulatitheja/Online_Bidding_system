"""onlinebidding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView

from user import views

urlpatterns = [
    path('userregister/',TemplateView.as_view(template_name="user/buyer_sellerregistration.html"),name='userregister'),
    path('successuser/',views.showsuccessuser,name='successuser'),
    path('userlogin/',views.showuserlogin,name='userlogin'),
    path('userwelcome/',TemplateView.as_view(template_name='user/userwelcome.html'),name="userwelcome"),
    path('sellproduct/',views.showsellproduct,name='sellproduct'),
    path('savesellproduct/',views.showsavesellproduct,name='savesellproduct'),
    path('buyproductpage/',views.showbuyproductpage,name='buyproductpage'),
    path('userlogout/',views.showuserlogout,name='userlogout'),
    path('savebidamount/',views.savebdammount,name='savebidamount'),
    path('bidtable/', views.bidTable, name='bidtable'),
    path('bidedproduct/',views.bidingmembersTable,name='bidedproduct'),
    path('stopbidding/',views.stopbidding,name='stopbidding'),
    path('purchasedproducts/',views.purchasedproducts,name='purchasedproducts'),
    # path('allbiding/',views.showallbidding,name='allbidding')



]
