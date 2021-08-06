import sys
sys.path.append("..")
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField

from users.models import User

class Department(models.Model):
    name= models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    manager=models.ForeignKey(User,on_delete=models.CASCADE,related_name='department', null=True)

    def __str__(self):
        return self.name
    
CATEGORY_CHOICES= (
    ("furniture", "furniture"),
    ("electronics", "electronics"),
    ("stationary", "stationary"),

)
class Asset(models.Model):
    name= models.CharField(max_length=50)
    description= models.TextField()
    image= CloudinaryField('image')
    department= models.ForeignKey('Department',on_delete=models.CASCADE,related_name='department_asset')
    category= models.CharField(max_length=50,choices=CATEGORY_CHOICES,default='furniture')
    created_at= models.DateTimeField(auto_now_add=True)
    modified_at= models.DateTimeField(auto_now=True)
    is_assigned= models.BooleanField(default=False)
 
    def __str__(self):
        return self.name
    
class EmployeeAsset(models.Model):
    employee = models.ForeignKey(User,on_delete=models.CASCADE,related_name='employee')
    asset= models.ForeignKey(Asset,on_delete=models.CASCADE,related_name='asset')
    def __str__(self):
        return self.employee.username
    
    
    
REQUESTTYPE_CHOICES = (
    ("new_asset", "new_asset"),
    ("repair", "repair"),
    ("replacement", "replacement"),

)
REQUEST_STATUS = (
    ("pending", "pending"),
    ("approved", "approved"),
    ("rejected", "rejected"),

)
class EmployeeAssetRequest(models.Model):
    employee=models.ForeignKey(User,on_delete=models.CASCADE,related_name='employee_asset_request')
    type= models.CharField(max_length=50,choices=REQUESTTYPE_CHOICES,default='new_asset')
    request_details= models.TextField()
    quantity= models.IntegerField(default=0)
    status=  models.CharField(max_length=50,choices=REQUEST_STATUS,default='pending')
    posted_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.request_details} employee_request'
    
class ManagerRequest(models.Model):
    request= models.TextField()
    specs= models.TextField()
    posted_date=models.DateTimeField(auto_now_add=True)
    status=  models.CharField(max_length=50,choices=REQUEST_STATUS,default='pending')
    employee=models.ForeignKey(User,on_delete=models.CASCADE,related_name='manager_request')
   
    def __str__(self):
        return f'{self.request} Manager_request'
    
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image', null=True)
    phone = models.IntegerField()
    bio = models.TextField(default='Bio...', max_length=100)
    department= models.ForeignKey('Department',on_delete=models.CASCADE,related_name='employee_department')

    def __str__(self):
        return f'{self.user.username} Profile'
