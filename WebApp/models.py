from django.db import models

# Create your models here.
class contactdb(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Phone = models.IntegerField(null=True,blank=True)
    Subject = models.CharField(max_length=100,null=True,blank=True)
    Message = models.TextField(max_length=100,null=True,blank=True)


class RegistrationDb(models.Model):
    Username = models.CharField(max_length=100,null=True,blank=True)
    Email_Id = models.EmailField(max_length=100,null=True,blank=True)
    Password = models.CharField(max_length=100,null=True,blank=True)
    Confirm_Password = models.CharField(max_length=100,null=True,blank=True)

class CartDb(models.Model):
    Username = models.CharField(max_length=100,blank=True,null=True)
    ProductName = models.CharField(max_length=100,blank=True,null=True)
    Quantity = models.IntegerField(blank=True,null=True)
    TotalPrice = models.IntegerField(blank=True,null=True)

class PaymentDb(models.Model):
    Name = models.CharField(max_length=100,blank=True,null=True)
    Email_Id = models.EmailField(max_length=100,blank=True,null=True)
    Address = models.CharField(max_length=100,blank=True,null=True)
    Phone_Number = models.IntegerField(blank=True,null=True)
    SaySomething = models.TextField(max_length=100,blank=True,null=True)
