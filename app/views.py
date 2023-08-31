from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from .models import *
from .forms import *
from app import models

def userLogin(request):
    data={}
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            request.session['username']=username
            return HttpResponseRedirect('view-all')
        else:
                data['error']="Username or Password is incorrect"
                res=render(request,'appl/user_login.html',data)
                return res
    else:
        return render(request,'appl/user_login.html',data)
    
def userLogout(request):
    logout(request)
    return HttpResponseRedirect('login')    

@login_required(login_url="login")
def deleteinventory(request):
    inventoryid=request.GET['inventoryid']
    item=models.inventory.objects.filter(id=inventoryid)
    item.delete()
    return HttpResponseRedirect('view-all')

@login_required(login_url="login")
def editinventory(request):
    item=models.inventory.objects.get(id=request.GET['inventoryid'])
    fields={'ProductId':item.ProductId,'ProductName':item.ProductName,'Vendor':item.Vendor
            ,'MRP':item.MRP,'BatchNum':item.BatchNum,'BatchDate':item.BatchDate,'Quantity':item.Quantity,
            'status':item.status}
    form=inventoryform(initial=fields)
    res=render(request,'appl/edit-inventory.html',{'item':item,'form':form})
    return res 

@login_required(login_url="login")
def edit(request):
    if request.method=="POST":
        form=inventoryform(request.POST)
        inventory=models.inventory()
        inventory.id=request.POST["inventoryid"]
        inventory.ProductId=form.data["ProductId"]
        inventory.ProductName=form.data["ProductName"]
        inventory.Vendor=form.data["Vendor"]
        inventory.MRP=form.data["MRP"]
        inventory.BatchNum=form.data["BatchNum"]
        inventory.BatchDate=form.data["BatchDate"]
        inventory.Quantity=form.data["Quantity"]
        inventory.status=form.data["status"]
        if form.is_valid:
            inventory.save()
            return HttpResponseRedirect("view-all")

@login_required(login_url="login")
def viewinventoryitems(request):
    item=models.inventory.objects.all()
    res=render(request,'appl/viewinventroy_item.html',{'item':item})
    return res

@login_required(login_url="login")
def addinventory(request):
    form=inventoryform()
    data={'form':form}
    res=render(request,"appl/addinventory.html",data)
    return res

@login_required(login_url="login")
def merge(request):
    if request.method=="POST":
        form=inventoryform(request.POST)
        inventory=models.inventory()
        inventory.ProductId=form.data["ProductId"]
        inventory.ProductName=form.data["ProductName"]
        inventory.Vendor=form.data["Vendor"]
        inventory.MRP=form.data["MRP"]
        inventory.BatchNum=form.data["BatchNum"]
        inventory.BatchDate=form.data["BatchDate"]
        inventory.Quantity=form.data["Quantity"]
        inventory.status=form.data["status"]
        if form.is_valid:
            inventory.save()
            s="Data stored successfully<br><a href='view-all'>View All Records</a>"
            return HttpResponse(s)
       



        