from django.shortcuts import render,redirect
from .models import formations,saved_squad,temp
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.urls import reverse,reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
import json
from django.views.decorators.csrf import csrf_exempt










def home(request):
    if request.user.is_authenticated:
        Li = False
    else:
        Li=True
    try:
        t = temp.objects.get(user=request.user)
        t.delete() 
    except:
        pass     
    else:
        pass    
    return render(request,"menu.html",{"f":formations.objects.all(),"Li":Li})



def loginpage(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:    
        if request.method=="POST":
            un = request.POST.get("username")
            ps = request.POST.get("password")
            user = authenticate(request,username=un,password=ps)
            if user is not None:
                login(request,user)
                return redirect("home")
            else:
                messages.info(request,'Invalid username or password , Try again')    


        return render(request,"login.html")


def logoutuser(request):
    logout(request)
    return redirect("home")


def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:    
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account is created for '+user)
                return redirect("login")    

    return render(request,"register.html",{"form":form , "errors":form.errors})





    #----------------------------------------

@login_required(login_url="login")
def creat_squad(request,formation):
    try:
        t = temp.objects.get(user=request.user)
        t.delete() 
    except:
        pass
    temp.objects.create(form = formations.objects.get(name=formation),user=request.user)
    t = temp.objects.get(user=request.user)
    form = t.form
    
    h=["p"+str(x) for x in range(1,12)]
    pl=[[],[],[],[],[],[]]
    l1 = [form.att,form.mid_att,form.mid_mid,form.mid_def,form.deff,1]
    c1=0
    c2=0
    i=0
    l3=[[],[],[],[],[],[]]
    for x in l1:
        c1=c2
        c2 +=x
        for y in h[c1:c2]:
            pl[i].append(y)
        i+=1  
    print(pl)      
    
    return render(request,"names.html",{"l":pl})


@login_required(login_url="login")
@csrf_exempt
def save_names(request):
        data = json.loads(request.body)
        t = temp.objects.get(user=request.user)
        l2 = [data["t1"],data["t2"],data["t3"],data["t4"],data["t5"],data["t6"],data["t7"],data["t8"],
        data["t9"],data["t10"],data["t11"]]
        t.names = ",".join(l2)
        t.save()
        print(l2)
        return JsonResponse("the names have been saved ",safe=False)

def display_squad(request):
        t = temp.objects.get(user=request.user)
        form = t.form
        l1 = [form.att,form.mid_att,form.mid_mid,form.mid_def,form.deff,1]
        l2 = t.names.split(",")
        c1=0
        c2=0
        i=0
        i2=1
        l3=[[],[],[],[],[],[]]
        for x in l1:
            c1=c2
            c2 +=x
            for y in l2[c1:c2]:
                l3[i].append([y,i2])
                i2+=1
            i+=1    
        print(l2)    
        return render(request,"field.html",{"l":l3})

    #----------------------------------------        








@login_required(login_url="login")
def savelist(request):
    if request.user.is_authenticated:
        Li = False
    else:
        Li=True
    s = saved_squad.objects.filter(user=request.user)    
    return render(request,"savelist.html",{"Li":Li,"s":s})

def savelist_display(request,sname):
    s = saved_squad.objects.filter(user=request.user)   
    us = s.get(name=sname)
    l1u = [us.formation.att,us.formation.mid_att,us.formation.mid_mid,us.formation.mid_def,us.formation.deff,1]
    l2u = [us.p1[us.p1.index("/")+2:len(us.p1)],us.p2[us.p2.index("/")+2:len(us.p2)],us.p3[us.p3.index("/")+2:len(us.p3)],us.p4[us.p4.index("/")+2:len(us.p4)],
    us.p5[us.p5.index("/")+2:len(us.p5)],us.p6[us.p6.index("/")+2:len(us.p6)],us.p7[us.p7.index("/")+2:len(us.p7)],us.p8[us.p8.index("/")+2:len(us.p8)],
    us.p9[us.p9.index("/")+2:len(us.p9)],us.p10[us.p10.index("/")+2:len(us.p10)],us.p11[us.p11.index("/")+2:len(us.p11)]]
    c1=0
    c2=0
    i=0
    i2=1
    l3=[[],[],[],[],[],[]]
    for x in l1u:
        c1=c2
        c2 +=x
        for y in l2u[c1:c2]:
            l3[i].append([y,i2])
            i2+=1
        i+=1    
        
    c = [us.p1[0:us.p1.index("/")-1],us.p2[0:us.p2.index("/")-1],us.p3[0:us.p3.index("/")-1],us.p4[0:us.p4.index("/")-1],
    us.p5[0:us.p5.index("/")-1],us.p6[0:us.p6.index("/")-1],us.p7[0:us.p7.index("/")-1],us.p8[0:us.p8.index("/")-1],
    us.p9[0:us.p9.index("/")-1],us.p10[0:us.p10.index("/")-1],us.p11[0:us.p11.index("/")-1]]
    print(c)
    return render(request,"saved.html",{"l":l3,"c":c,"us":us})

@csrf_exempt
def delete(request):
    data = json.loads(request.body)
    u = saved_squad.objects.filter(user=request.user)
    u.get(name=data["sname"]).delete()
    return JsonResponse("the cordinates have been saved ",safe=False)

@csrf_exempt
def save(request):
        t = temp.objects.get(user=request.user)
        form = t.form
        data = json.loads(request.body)
        saved_squad.objects.create(p1=data["t1"],p2=data["t2"],p3=data["t3"],p4=data["t4"],
        p5=data["t5"],p6=data["t6"],p7=data["t7"],p8=data["t8"],p9=data["t9"],
        p10=data["t10"],p11=data["t11"],name=data["sname"],formation=form,user=request.user)
        saved_squad.save
        return JsonResponse("the cordinates have been saved ",safe=False)

