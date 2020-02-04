from django.shortcuts import render,redirect
from user.models import UserregisterModel
from badmin.models import AdminModel
from django.contrib import messages
from badmin.smsprocess import smsprocess

# Create your views here.
def showadminwelcome(request):
    uname = request.POST['uname']
    upass = request.POST['upass']
    try:

        res = AdminModel.objects.get(uname=uname,upass=upass)
        request.session['name'] = res.uname
        return render(request,'badmin/adminwelcome.html')
    except:
        messages.error(request,"invalied Username/Password")
        return redirect('adminloginpage')


def showpendingusers(request):
    data = UserregisterModel.objects.filter(status="pending")
    return render(request,"badmin/pending.html",{"mess":data})


def showapprovedusers(request):
    data = UserregisterModel.objects.filter(status="approved")
    return render(request,'badmin/approved.html',{"mess":data})


def showdeclineusers(request):
    data = UserregisterModel.objects.filter(status="decline")
    return render(request, 'badmin/decline.html', {"mess": data})


def showlogout(request):
        del request.session['name']
        return redirect('adminloginpage')

def showapproveusers(request):
    idno = request.POST['a1']
    qs = UserregisterModel.objects.filter(idno=idno)
    nam = ""
    con = ""
    for x in qs:
       nam = x.name
       con = x.contact
    qs.update(status='approved')
    mess = "Hello Mr/Miss : "+nam+"Your Registration is approved"
    x = smsprocess(str(con),mess)
    print(x)
    return redirect('pendinguser')


def showdecline(request):
    idno = request.POST['a2']
    qs = UserregisterModel.objects.filter(idno=idno)
    nam = ''
    con = ''
    for x in qs:
        nam = x.name
        con = x.contact
    qs.update(status ='decline')
    mess = "Hello Mr/Miss : "+nam+" Your Registration is Declined"
    x = smsprocess(str(con),mess)
    print(x)
    return redirect('pendinguser')


