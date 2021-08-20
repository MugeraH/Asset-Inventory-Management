import sys

from django.db.models.fields import EmailField
sys.path.append("..")
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField

from users.models import User

class Department(models.Model):
    name= models.CharField(max_length=50)
    description=models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    manager=models.ForeignKey(User,on_delete=models.CASCADE,related_name='department_manager', null=True)
    
    class Meta:
        ordering = ["pk"]

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

    department= models.ForeignKey('Department',on_delete=models.CASCADE,related_name='asset_department',null=True)

    category= models.CharField(max_length=50,choices=CATEGORY_CHOICES,default='furniture')
    created_at= models.DateTimeField(auto_now_add=True) 
    updated_date= models.DateTimeField(auto_now=True)
    is_assigned_dept= models.BooleanField(default=False)
    is_assigned_user= models.BooleanField(default=False)
    
    class Meta:
        ordering = ["pk"]

    def __str__(self):
        return self.name
    
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

ROLES = (
    ("Admin", "Admin"),
    ("Employee", "Employee"),

)
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image', null=True)
    phone = models.IntegerField(default="07100")
    bio = models.TextField(default='Bio...', max_length=100)
    department= models.ForeignKey('Department',on_delete=models.CASCADE,related_name='employee_department',null=True)
    role =  models.CharField(max_length=50,choices=ROLES ,default='Employee')

    class Meta:
        ordering = ["pk"]
    def __str__(self):
        return f'{self.user.username} Profile'
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()
    
    @classmethod
    def filter_profile_by_id(cls, id):
        profile = Profile.objects.filter(user__id = id).first()
        return profile

class Email(models.Model):
    full_name = models.CharField(max_length=100)
    email = EmailField()
    account_specifications = models.TextField()

    def __str__(self):
        return self.full_name
class EmployeeAsset(models.Model):
    employee = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='employee_det',null=True)
    asset= models.ForeignKey(Asset,on_delete=models.CASCADE,related_name='asset_user')
    
    class Meta:
        ordering = ["pk"]
    def __str__(self):
        return self.asset.name
    
    
def post_asset_created_signal(sender,instance,created, **kwargs):
        print(instance,created)
        if created:
            EmployeeAsset.objects.create(asset=instance) 
post_save.connect(post_asset_created_signal,sender = Asset)


URGENCY = (
    ("1", "high"),
    ("2", "medium"),
    ("3", "low"),

)

class EmployeeAssetRequest(models.Model):
    employee=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='employee_asset_request',null=True)
    type= models.CharField(max_length=50,choices=REQUESTTYPE_CHOICES,default='new_asset')
    request_detail= models.TextField()
    quantity= models.IntegerField(default=0)
    status=  models.CharField(max_length=50,choices=REQUEST_STATUS,default='pending')
    posted_date=models.DateTimeField(auto_now_add=True)
    urgency = models.CharField(max_length=50,choices=URGENCY,default='urgency')
    completed= models.BooleanField(default=False)
    

    class Meta:
        ordering = ["urgency"]

    def __str__(self):
        return f'{self.request_detail} employee_request'
    
class ManagerRequest(models.Model):
    request= models.TextField()
    specs= models.TextField()
    quantity= models.IntegerField(default=0)
    posted_date=models.DateTimeField(auto_now_add=True)
    status=  models.CharField(max_length=50,choices=REQUEST_STATUS,default='pending')
    employee=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='manager_request',null=True)
    urgency = models.CharField(max_length=50,choices=URGENCY,default='urgency2')
    completed= models.BooleanField(default=False)

    class Meta:
        ordering = ["urgency"]

        
    def __str__(self):
        return f'{self.request} Manager_request'
