from django.db import models

# Create your models here.

class categorydb(models.Model):
    Category_Name = models.CharField(max_length=100,blank=True,null=True)
    Description = models.TextField(max_length=100,blank=True,null=True)
    Category_Image = models.ImageField(upload_to="Category Image",null=True,blank=True)

class productdb(models.Model):
    Category = models.CharField(max_length=100,blank=True,null=True)
    Product_Name = models.CharField(max_length=100,blank=True,null=True)
    Price = models.IntegerField(null=True,blank=True)
    Description = models.TextField(max_length=100,null=True,blank=True)
    Product_Image = models.ImageField(upload_to="Product Images",null=True,blank=True)
