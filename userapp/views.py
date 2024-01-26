from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import signup_tbl,Record

from .forms import CreateRecordForm, UpdateRecordForm,EmailForm

from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method=='POST':
        name=request.POST.get('nm')
        email=request.POST.get('em')
        phone=request.POST.get('pn')
        newps=request.POST.get('np')
        cnfrmps=request.POST.get('cp')
        if newps != cnfrmps:
            return HttpResponse("your passwords didn't match")
        else:
            obj=signup_tbl.objects.create(nm=name,em=email,pn=phone,np=newps,cp=cnfrmps)
            obj.save()
            return redirect('login')
    else:
        return render(request,'signup.html')

def about(request):
    return render(request,'about.html')

def login(request):
    if request.method=='POST':
        eml=request.POST.get('em')
        psw=request.POST.get('np')
        obj=signup_tbl.objects.filter(em=eml,np=psw)
        if obj:
            request.session['ema']=eml
            request.session['psa']=psw
            for ls in obj:
                idno=ls.id
                request.session["idn"]=idno

            return render(request,'dashboard.html')
        else:
            msg="Invalid Email or Password !"
            request.session['ema']=''
            request.session['psa']=''
            return render(request,'login.html',{'error':msg})
    else:
        return render(request,'login.html')


def dashboard(request):
    obj=signup_tbl.objects.all()
    return render(request,"dashboard.html",{"view":obj})


def profile(request):
    return render(request,'profile.html')


def task(request):
    return render(request,'task.html')


def teams(request):
    my_records=Record.objects.all()
    return render(request,'teams.html',{"data":my_records})

# create a reocord

def create_record(request):
    form= CreateRecordForm()
    if request.method=="POST":
        form=CreateRecordForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("teams")
        
    context={'form':form}
    return render(request,'create-record.html',context=context)


# update a record

def update_record(request,pk):

    record=Record.objects.get(id=pk)
    form=UpdateRecordForm(instance=record)
    if request.method=='POST':
        form=UpdateRecordForm(request.POST,instance=record)
        if form.is_valid():
            form.save()
            return redirect("teams")
    
    context={'form':form}
    return render(request,'update-record.html',context=context)
    

# read/view a single record

def view_record(request,pk):
    all_records=Record.objects.get(id=pk)
    context={'record':all_records}
    return render(request,'view-record.html',context=context)

# Delete a record
def delete_record(request,pk):
    record=Record.objects.get(id=pk)
    record.delete()
    return redirect("teams")

def trans(request):
    return render(request,'transaction.html')


def settings(request):
    return render(request,'settings.html')

def email(request):
    form=EmailForm()
    if request.method=='POST':
        form=EmailForm(request.POST)
        if form.is_valid():
            sender=form.cleaned_data("email")
            sub = request.POST.get("subject")
            msg=request.POST.get("message")
        send_mail(sub,msg,settings.EMAIL_HOST_USER,[sender],fail_silently=False)
        success="Email sended successfully"
        return render(request,"email.html",{"success":success})
    else:
        return render(request,"email.html")