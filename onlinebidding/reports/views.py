from django.shortcuts import render,HttpResponse
from user.models import SellProductModel,BidtableModel,UserregisterModel

# Create your views here.
def showreportspage(request):
    return render(request,'reports/repotspage.html')

from django.db.models import Q
def showdailyreportspage(request):
    qs1 = SellProductModel.objects.filter(status='sold').values('user_id','user_id__bidtablemodel__productid_id')
    qs = SellProductModel.objects.filter(status='sold').values('user_id').values_list('bidtablemodel__date_of_join','user_id')[::-1][1]
    print(qs)

    return render(request,'reports/dailyreports.html',)