from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import login as log
from .models import user as usr
from .models import Products as product
from .models import staff as stafff


# Create your views here.

def index(request): 
    data=product.objects.all()
    return render(request,"index.html",{"data":data})
def contact(request): 
    return render(request,"contact.html")
def about(request): 
    return render(request,"about.html")
def shop(request): 
    return render(request,"shop.html")
def blog(request): 
    return render(request,"blog.html")
def faq(request): 
    return render(request,"faq.html")
def login(request):
    return render(request,"login.html")
def customer(request):
    return render(request,"customer.html")
def staff(request):
    return render(request,"staff.html")
def cart(request):
    return render(request,"cart.html")
def adminhome(request):
    return render(request,"adminhome.html")
def data(request):
    return render(request,"data.html")
def addproduct(request):
    return render(request,"addproduct.html")

@staff_member_required
def dashboard(request):
    """Enhanced dashboard with statistics and admin links"""
    # Get statistics
    total_users = usr.objects.count()
    total_staff = stafff.objects.count()
    total_products = product.objects.count()
    total_logins = log.objects.count()
    
    # Get pending approvals
    pending_users = usr.objects.filter(status='waiting').count()
    pending_staff = stafff.objects.filter(status='waiting').count()
    
    # Get recent data
    recent_users = usr.objects.order_by('-user_id')[:5]
    recent_products = product.objects.order_by('-id')[:5]
    
    context = {
        'total_users': total_users,
        'total_staff': total_staff,
        'total_products': total_products,
        'total_logins': total_logins,
        'pending_users': pending_users,
        'pending_staff': pending_staff,
        'recent_users': recent_users,
        'recent_products': recent_products,
    }
    return render(request, "dashboard.html", context)

def staff_dashboard(request):
    """Staff-specific dashboard"""
    # Check if user is logged in and is staff
    if 'logid' not in request.session or 'role' not in request.session:
        return redirect('login')
    
    if request.session['role'] != 'staff':
        return redirect('login')
    
    try:
        # Get staff information
        logd = log.objects.get(logid=request.session['logid'])
        staff_obj = stafff.objects.get(login=logd)
        
        # Get staff-specific data
        total_products = product.objects.count()
        recent_products = product.objects.order_by('-id')[:5]
        
        context = {
            'staff': staff_obj,
            'total_products': total_products,
            'recent_products': recent_products,
        }
        return render(request, "staff_dashboard.html", context)
        
    except (log.DoesNotExist, stafff.DoesNotExist):
        return redirect('login')

def adminlogin(request):
    if request.method == 'POST':
        t1 = request.POST.get("username")
        t2 = request.POST.get("password")
        
        try:
            logd = log.objects.get(username=t1, password=t2)
            
            # Set session data
            request.session["logid"] = logd.logid
            request.session["role"] = logd.role
            request.session["username"] = t1
            
            # Redirect based on role
            if logd.role == "admin":
                return redirect('/adminhome')
            elif logd.role == "staff":
                # Check if staff is approved
                try:
                    staff_obj = stafff.objects.get(login=logd)
                    if staff_obj.status == "approved":
                        return redirect('/staff-dashboard')  # Staff goes to staff dashboard
                    else:
                        msg = "Your staff account is pending approval. Please contact administrator."
                        return render(request, "login.html", {"msg": msg})
                except stafff.DoesNotExist:
                    msg = "Staff profile not found. Please contact administrator."
                    return render(request, "login.html", {"msg": msg})
            elif logd.role == "customer":
                # Check if customer is approved
                try:
                    user_obj = usr.objects.get(login=logd)
                    if user_obj.status == "approved":
                        return redirect('/customer-dashboard')  # Customer goes to customer dashboard
                    else:
                        msg = "Your account is pending approval. Please contact administrator."
                        return render(request, "login.html", {"msg": msg})
                except usr.DoesNotExist:
                    msg = "User profile not found. Please contact administrator."
                    return render(request, "login.html", {"msg": msg})
            else:
                msg = "Invalid user role. Please contact administrator."
                return render(request, "login.html", {"msg": msg})
                
        except log.DoesNotExist:
            msg = "Invalid username or password"
            return render(request, "login.html", {"msg": msg})
    
    # If not POST request, show login page
    return render(request, "login.html")
    
   # _______---Customer registraion function--_____

def customerreg(request):
     fullname=request.POST["fullname"]
     address=request.POST["address"]
     mobileno=request.POST["mobileno"]
     mail=request.POST["mail"]
     username=request.POST["username"]
     password=request.POST["password"]
     
     log.objects.create(username=username,password=password,role="customer")
     data=log.objects.last()
     usr.objects.create(login=data,fullname=fullname,addr=address,mail=mail,mobileno=mobileno,status="waiting")
     response=redirect("login")
     return response 

# _______---Staff registraion function--_____

def staffreg(request):
     fullname=request.POST["fullname"]
     address=request.POST["address"]
     mobileno=request.POST["mobileno"]
     mail=request.POST["mail"]
     username=request.POST["username"]
     password=request.POST["password"]
     aadhar=request.POST["aadhar"]
     
     log.objects.create(username=username,password=password,role="staff")
     data=log.objects.last()
     stafff.objects.create(login=data,fullname=fullname,aadhar=aadhar,addr=address,mail=mail,mobileno=mobileno,status="waiting")
     response=redirect("adminhome")
     return response 

def data(request):
     data=usr.objects.all()
     return render(request,"data.html",{"data":data})

def staffdata(request):
     data=stafff.objects.all()
     return render(request,"staffdata.html",{"data":data})

# _______---Adding Products to DB function--_____

def addproducts(request):
     pn=request.POST["pn"]
     pq=request.POST["pq"]
     pp=request.POST["pp"]
     pc=request.POST["pc"]
     pi=request.FILES["pi"]  
     product.objects.create(pn=pn,pq=pq,pp=pp,pc=pc,pi=pi)
     response=redirect("adminhome")
     return response 

def productdata(request):
     data=product.objects.all()
     return render(request,"productdata.html",{"data":data})

def pdts(request):
     data=product.objects.all()
     return render(request,"productdata.html",{"data":data})

def customer_dashboard(request):
    """Customer-specific dashboard"""
    # Check if user is logged in and is customer
    if 'logid' not in request.session or 'role' not in request.session:
        return redirect('login')
    
    if request.session['role'] != 'customer':
        return redirect('login')
    
    try:
        # Get customer information
        logd = log.objects.get(logid=request.session['logid'])
        user_obj = usr.objects.get(login=logd)
        
        # Get customer-specific data
        total_products = product.objects.count()
        recent_products = product.objects.order_by('-id')[:6]
        
        context = {
            'customer': user_obj,
            'total_products': total_products,
            'recent_products': recent_products,
        }
        return render(request, "customer_dashboard.html", context)
        
    except (log.DoesNotExist, usr.DoesNotExist):
        return redirect('login')

def logout_view(request):
    """Handle user logout"""
    # Clear session data
    request.session.flush()
    return redirect('login')

