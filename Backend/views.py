from django.shortcuts import render,redirect
from Backend.models import categorydb,productdb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from WebApp.models import contactdb
from django.contrib import messages

# Create your views here.

def index_page(request):
    return render(request,'index.html')

def category_page(request):
    return render(request,'category.html')

def save_category(request):
    if request.method == "POST":
        c_na = request.POST.get('c_name')
        des = request.POST.get('description')
        img = request.FILES['image']
        obj = categorydb(Category_Name=c_na,Description=des,Category_Image=img)
        obj.save()
        messages.success(request,"Category Saved Successfully...!")
        return redirect(category_page)

def display_category(request):
    data = categorydb.objects.all()
    return render(request,'display_category.html',{'data':data})

def edit_category(request,cat_id):
    data = categorydb.objects.get(id=cat_id)
    return render(request,'edit_category.html',{'data':data})

def update_category(request,cat_id):
    if request.method == "POST":
        c_na = request.POST.get('c_name')
        des = request.POST.get('description')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = categorydb.objects.get(id=cat_id).Category_Image
    categorydb.objects.filter(id=cat_id).update(Category_Name=c_na,Description=des,Category_Image=file)
    messages.success(request,"Successfully Updated...!")
    return redirect(display_category)

def delete_category(request,cat_id):
    data = categorydb.objects.filter(id=cat_id)
    data.delete()
    messages.error(request,"Deleted...!")
    return redirect(display_category)

def login_page(request):
    return render(request,'admin_login.html')

def admin_login(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pwd = request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un,password=pwd)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=pwd
                messages.success(request,"Welcome..!")
                return redirect(index_page)
            else:
                messages.error(request,"Invalid Password")
                return redirect(login_page)
        else:
            messages.warning(request,"User not found!")
            return redirect(login_page)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request,"Logout Successfull..!")
    return redirect(login_page)


def product_page(request):
    cat = categorydb.objects.all()
    return render(request,"products.html",{'cat':cat})

def save_product(request):
    if request.method == "POST":
        c_na = request.POST.get('c_name')
        p_na = request.POST.get('p_name')
        pri = request.POST.get('price')
        des = request.POST.get('description')
        p_img = request.FILES['p_image']
        obj = productdb(Category=c_na,Product_Name=p_na,Price=pri,Description=des,Product_Image=p_img)
        obj.save()
        messages.success(request,"Product Saved Sucessfully...!")
        return redirect(product_page)

def display_product(request):
    data = productdb.objects.all()
    return render(request,'display_product.html',{'data':data})


def edit_product(request,pro_id):
    pro = productdb.objects.get(id=pro_id)
    cat = categorydb.objects.all()
    return render(request,'edit_product.html',{'pro':pro,'cat':cat})

def update_product(request,pro_id):
    if request.method == "POST":
        c_na = request.POST.get('c_name')
        p_na = request.POST.get('p_name')
        pri = request.POST.get('price')
        des = request.POST.get('description')
        try:
            p_img = request.FILES['p_image']
            fs = FileSystemStorage()
            file = fs.save(p_img.name,p_img)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=pro_id).Product_Image
        productdb.objects.filter(id=pro_id).update(Category=c_na,Product_Name=p_na,Price=pri,Description=des,Product_Image=file)
        messages.success(request,"Products Updated...!")
        return redirect(display_product)

def delete_product(request,pro_id):
    pro = productdb.objects.filter(id=pro_id)
    pro.delete()
    messages.error(request,"Product Deleted...!")
    return redirect(display_product)

def contact_details(request):
    data = contactdb.objects.all()
    return render(request,'ContactData.html',{'data':data})

def delete_enquiry(request,con_id):
    data = contactdb.objects.filter(id=con_id)
    data.delete()
    return redirect(contact_details)