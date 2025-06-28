from django.db import models

# Create your models here.

# _______---Login Details--_____

class login(models.Model):
   logid = models.AutoField(primary_key=True)
   username = models.CharField("Username", max_length=15, unique=True)
   password = models.CharField("Password", max_length=15)  
   role = models.CharField("Role", max_length=15, choices=[
       ('admin', 'Admin'),
       ('customer', 'Customer'),
       ('staff', 'Staff'),
   ])
   
   class Meta:
       verbose_name = "Login"
       verbose_name_plural = "Logins"
       db_table = 'flower_login'
   
   def __str__(self):
       return f"{self.username} ({self.role})"
   
# _______---User Details--_____

class user(models.Model):
   user_id = models.AutoField(primary_key=True)
   login = models.ForeignKey(login, on_delete=models.CASCADE, null=True, verbose_name="Login")
   fullname = models.CharField("Full Name", max_length=100)
   addr = models.CharField("Address", max_length=100)
   mobileno = models.CharField("Mobile Number", max_length=100)
   mail = models.CharField("Email", max_length=100)  
   status = models.CharField("Status", max_length=100, choices=[
       ('waiting', 'Waiting'),
       ('approved', 'Approved'),
       ('rejected', 'Rejected'),
   ])
   
   class Meta:
       verbose_name = "User"
       verbose_name_plural = "Users"
       db_table = 'flower_user'
   
   def __str__(self):
       return self.fullname

# _______---Staff Details--_____

class staff(models.Model):
   user_id = models.AutoField(primary_key=True)
   login = models.ForeignKey(login, on_delete=models.CASCADE, null=True, verbose_name="Login")
   fullname = models.CharField("Full Name", max_length=100)
   addr = models.CharField("Address", max_length=100)
   mobileno = models.CharField("Mobile Number", max_length=100)
   mail = models.CharField("Email", max_length=100)  
   status = models.CharField("Status", max_length=100, choices=[
       ('waiting', 'Waiting'),
       ('approved', 'Approved'),
       ('rejected', 'Rejected'),
   ])
   aadhar = models.CharField("Aadhar Number", max_length=100, default="0000000")  

   class Meta:
       verbose_name = "Staff"
       verbose_name_plural = "Staff"
       db_table = 'flower_staff'
   
   def __str__(self):
       return self.fullname

# _______---Products Details --_____

class Products(models.Model):
   pn = models.CharField("Product Name", max_length=100)
   pq = models.CharField("Product Quantity", max_length=100)
   pp = models.CharField("Product Price", max_length=100)
   pc = models.CharField("Product Category", max_length=100)  
   pi = models.FileField("Product Image", max_length=100, upload_to="images/")
   
   class Meta:
       verbose_name = "Product"
       verbose_name_plural = "Products"
       db_table = 'flower_products'
   
   def __str__(self):
       return self.pn





