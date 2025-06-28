from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .import views
urlpatterns=[
    path("",views.index,name="index"),
    path("index",views.index,name="index"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("shop",views.shop,name="shop"),
    path("blog",views.blog,name="blog"),
    path("faq",views.faq,name="faq"),
    path("login",views.login,name="login"),
    path("logout",views.logout_view,name="logout"),
    path("customer",views.customer,name="customer"),
    path("staff",views.staff,name="staff"),
    path("cart",views.cart,name="cart"),
    path("adminlogin",views.adminlogin,name="adminlogin"),
    path("adminhome",views.adminhome,name="adminhome"),
    path("dashboard",views.dashboard,name="dashboard"),
    path("staff-dashboard",views.staff_dashboard,name="staff_dashboard"),
    path("customerreg",views.customerreg,name="customerreg"),
    path("staffreg",views.staffreg,name="staffreg"),
    path("data",views.data,name="data"),
    path("staffdata",views.staffdata,name="staffdata"),
    path("addproduct",views.addproduct,name="addproduct"),
    path("addproducts",views.addproducts,name="addproducts"),
    path("productdata",views.productdata,name="productdata"),
    path("pdts",views.pdts,name="pdts"),
    
    

    




]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)