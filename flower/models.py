from django.db import models

# Create your models here.

# _______---Login Details--_____


class login(models.Model):
   logid=models.AutoField(primary_key=True)
   username=models.CharField("username",max_length=15)
   password=models.CharField("password",max_length=15)  
   role=models.CharField("role",max_length=15)
   
# _______---User Details--_____

class user(models.Model):
   user_id=models.AutoField(primary_key=True)
   login=models.ForeignKey(login,on_delete=models.CASCADE,null=True)
   fullname=models.CharField("fullname",max_length=100)
   addr=models.CharField("address",max_length=100)
   mobileno=models.CharField("mobileno",max_length=100)
   mail=models.CharField("email",max_length=100)  
   status=models.CharField("status",max_length=100)


   
# _______---Staff Details--_____



class staff(models.Model):
   user_id=models.AutoField(primary_key=True)
   login=models.ForeignKey(login,on_delete=models.CASCADE,null=True)
   fullname=models.CharField("fullname",max_length=100)
   addr=models.CharField("address",max_length=100)
   mobileno=models.CharField("mobileno",max_length=100)
   mail=models.CharField("email",max_length=100)  
   status=models.CharField("status",max_length=100)
   aadhar=models.CharField("aadhar",max_length=100,default=0000000)  

# _______---Products Details --_____


class Products(models.Model):
   pn=models.CharField("pn",max_length=100)
   pq=models.CharField("pq",max_length=100)
   pp=models.CharField("pp",max_length=100)
   pc=models.CharField("pc",max_length=100)  
   pi=models.FileField("pi",max_length=100,upload_to="images/")





