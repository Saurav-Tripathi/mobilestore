from django.shortcuts import render,redirect
from .models import Cart, Category, Product, Registration

# Create your views here.

def about(request):
    return render(request,"about.html")

def index(request):
    all_pro = Product.objects.all()[:8]
    prod = Product.objects.all()[1::4]


    con = {"all_pro":all_pro,"prod":prod}
    
    return render(request,"index.html",con)

def base(request):
    return render(request,"base.html")

def blog_default(request):
    return render(request,"blog-default.html")    

def blog_single(request):
    return render (request,"blog-single.html")    

def cart(request):
    return render (request,"cart.html")    

def checkout(request):
    return render (request,"checkout.html")    

def contact_us(request):
    return render(request,"contact-us.html")    

def login_form(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        try:
            valid = Registration.objects.get(email=email)
            if valid.password == password:
                request.session['user']=email
                request.session['user_name']=valid.name
                return redirect("index")
            else:
                return redirect("login_form")
        except:
            return redirect("login_form")
    return render(request,"login-form.html")    

def logout(request):
    if 'user' in request.session:
        del request.session['user']
        return redirect("login_form")
    return redirect("login_form")

def product_list(request):
    x = request.GET.get("cid")
    cat = Category.objects.all()

    product = Product.objects.filter(cat__name = x)

    return render(request,"product-list.html",{'cat':cat,"product":product})

def product_single(request,id):
    single = Product.objects.get(id=id)
    return render(request,"product-single.html",{'prod':single})



def signup_form(request):
    if request.method == "POST":
        name = request.POST["name"]
        number = request.POST["number"]
        email = request.POST["email"]
        password = request.POST["password"]
        con_password = request.POST["con_password"]
        if password == con_password:
            obj = Registration(name=name,number=number,email=email,password=password)
            obj.save()
            return redirect("login_form")
        else:
            return redirect("signup_form")
    return render(request,"signup-form.html")



def styleguide(request):
    return render(request,"styleguide.html")
    
def add_to_cart(request,id):
    if 'user' in request.session:
        user = request.session['user']
        us = Registration.objects.get(email=user)
        prod = Product.objects.get(id=id)
        qty = 1
        if prod:
            subtotal = prod.dis_price
            x = Cart(user=us,prod=prod,quantity=qty,subtotal=subtotal)
            x.save()
    return render(request, 'cart.html')                   