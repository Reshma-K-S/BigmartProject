from django.shortcuts import render,redirect
from Backend.models import productdb,categorydb
from WebApp.models import contactdb,RegistrationDb,CartDb
from django.contrib import messages

# Create your views here.
def home_page(request):
    cat = categorydb.objects.all()
    return render(request,'Home.html',{'cat':cat})


def about_page(request):
    cat = categorydb.objects.all()
    return render(request,'About.html',{'cat':cat})

def contact_page(request):
    cat = categorydb.objects.all()
    return render(request,'Contact.html',{'cat':cat})

def ourproduct(request):
    pro = productdb.objects.all()
    cat = categorydb.objects.all()
    return render(request,'OurProduct.html',{'pro':pro,'cat':cat})

def save_contact(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        ph = request.POST.get('phone')
        sub = request.POST.get('subject')
        mes = request.POST.get('message')
        obj = contactdb(Name=na,Email=em,Phone=ph,Subject=sub,Message=mes)
        obj.save()
        return redirect(contact_page)

def filter_products(request,cat_name):
    cat = categorydb.objects.all()
    data = productdb.objects.filter(Category=cat_name)
    return render(request,'Products_Filtered.html',{'data':data,'cat':cat})

def single_product(request,pro_id):
    cat = categorydb.objects.all()
    data = productdb.objects.get(id=pro_id)
    return render(request,'Single_Product.html',{'data':data,'cat':cat})

def registration_page(request):
    return render(request,'Registration.html')

def save_register(request):
    if request.method == "POST":
        na = request.POST.get('username')
        em = request.POST.get('email')
        pas = request.POST.get('password')
        pas1 = request.POST.get('pass')
        obj = RegistrationDb(Username=na,Email_Id=em,Password=pas,Confirm_Password=pas1)
        if RegistrationDb.objects.filter(Username=na).exists():
            messages.warning(request,"Username already exists..!")
            return redirect(registration_page)
        elif RegistrationDb.objects.filter(Email_Id=em).exists():
            messages.warning(request,"Email Id already exists..!")
            return redirect(registration_page)
        else:
            obj.save()
            messages.success(request,"Registration Successfull..!")
        return redirect(registration_page)


def Userlogin(request):
    if request.method == "POST":
        un = request.POST.get('uname')
        pswd = request.POST.get('pwd')
        if RegistrationDb.objects.filter(Username=un,Password=pswd).exists():
            request.session['Username'] = un
            request.session['Password'] = pswd
            messages.success(request,"WELCOME")
            return redirect(home_page)
        else:
            messages.error(request,"Invalid Username!")
            return redirect(registration_page)
    else:
        messages.warning(request,"User not found!")
        return redirect(registration_page)

def User_logout(request):
    del request.session['Username']
    del request.session['Password']
    messages.success(request,"Logout Successfull")
    return redirect(home_page)

def save_cart(request):
    if request.method == "POST":
        user_na = request.POST.get("userna")
        product_na = request.POST.get("productna")
        qua = request.POST.get("quantity")
        t_pri = request.POST.get("tprice")
        obj = CartDb(Username=user_na,ProductName=product_na,Quantity=qua,TotalPrice=t_pri)
        obj.save()
        messages.success(request,"Item added to cart!")
        return redirect(home_page)

def cart_page(request):
    data = CartDb.objects.filter(Username=request.session['Username'])
    cat = categorydb.objects.all()
    total = 0
    for d in data:
        total = total + d.TotalPrice
    return render(request,"Cart.html",{'data':data,'total':total,'cat':cat})

def delete_item(request,cart_id):
    x = CartDb.objects.filter(id=cart_id)
    x.delete()
    messages.error(request,"Item removed from cart")
    return redirect(cart_page)

def user_login_page(request):
    return render(request,"User_login.html")
