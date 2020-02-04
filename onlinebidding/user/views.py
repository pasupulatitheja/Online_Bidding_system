from django.shortcuts import render, redirect
from .models import UserregisterModel, SellProductModel, BidtableModel
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.

def showsuccessuser(request):
    try:
        name = request.POST['name']
        contact = request.POST['contact']
        email = request.POST['email']
        password = request.POST['password']
        status = "pending"
        UserregisterModel(name=name, contact=contact, email=email, password=password, status=status).save()
        messages.success(request, "Register Succssfully And Admin Need To Approved")
        return redirect('userregister')
    except:
        messages.error(request, "Invalied Contact/Email-Id Already Used")
        return redirect('userregister')


def showuserlogin(request):
    uname = request.POST['s1']
    upass = request.POST['s2']
    try:
        res = UserregisterModel.objects.get(email=uname, password=upass)
        if res.status == 'approved':
            request.session['username'] = res.name
            request.session['userid'] = res.idno
            return render(request, 'user/userwelcome.html')
        elif res.status == 'pending':
            messages.error(request, 'Your request is pending')
            return redirect('userregister')
        else:
            messages.error(request, 'Your registation is Declined')
            return redirect('userregister')
    except UserregisterModel.DoesNotExist:
        messages.error(request, "Your Not Registerd need to Register")
        return redirect('userregister')


def showsavesellproduct(request):
    name = request.POST['p1']
    price = request.POST['p2']
    info = request.POST['p3']
    pimage = request.FILES['p4']
    status = 'bidding'
    userid = request.session['userid']
    SellProductModel(pname=name, bid_price=price, info=info, p_image=pimage, status=status, user_id_id=userid).save()
    messages.success(request, "Product is Saved")
    return redirect(showsellproduct)


def showsellproduct(request):
    pgno = request.GET.get('pgno')
    data = SellProductModel.objects.filter(status='bidding',user_id_id=request.session['userid'])
    result = Paginator(data,4)
    if pgno:
        page = result.page(int(pgno))
    else:
        page = result.page(1)
    return render(request, 'user/sellproductpage.html',{"data": page})



def showbuyproductpage(request):
    pgno = request.GET.get('pgno')
    res = SellProductModel.objects.filter(status='bidding') & SellProductModel.objects.filter(
        ~Q(user_id_id=request.session['userid']))
    result = Paginator(res,3)
    if pgno:
        page = result.page(int(pgno))
    else:
        page = result.page(1)
    return render(request, 'user/buyproduct.html', {"data": page})


def showuserlogout(request):
    del request.session['username']
    return redirect('userwelcome')


def savebdammount(request):
    bamount = request.POST['b1']
    uid = request.POST['b2']
    pid = request.POST['b3']
    BidtableModel(bid_ammount=bamount,userid_id=uid,productid_id=pid).save()
    res = BidtableModel.objects.filter(productid_id=pid)
    return render(request, 'user/showbidtable.html', {'data': res,'pidno':pid})

def bidTable(request):
    pid = request.GET.get('clickid')
    res = BidtableModel.objects.filter(productid_id=pid)
    return render(request,'user/showbidtable.html',{'data':res,'pidno':pid,})


def bidingmembersTable(request):
    pid = request.GET.get('p1')
    res = BidtableModel.objects.filter(productid_id=pid)
    return render(request,'user/bidingmembertable.html', {'data': res,'pid':pid})


def stopbidding(request):
    pid = request.POST['productid']
    uid = request.POST['userid']
    res = SellProductModel.objects.filter(id=pid)
    res.update(status='sold',user_id_id=uid)
    messages.success(request,'Bidding is stoped')
    return bidingmembersTable(request)


def purchasedproducts(request):
    # userid = request.GET.get('userid')
    res1 = SellProductModel.objects.filter(status='sold',user_id_id=request.session['userid'])
    # res2 = BidtableModel.objects.filter(user_id_id=userid)
    # print(res2)
    return render(request,'user/purchasedproduct.html',{'products':res1,})