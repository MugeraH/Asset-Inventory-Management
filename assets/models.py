from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=50)
    created_at= models.DateTimeField(auto_now_add=True)
    modified_at= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class Department(models.Model):
    name= models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Asset(models.Model):
    name= models.CharField(max_length=50)
    description= models.TextField()
    image= CloudinaryField('image')
    category= models.ForeignKey('Category',on_delete=models.CASCADE,related_name='asset')
    department= models.ForeignKey('Department',on_delete=models.CASCADE,related_name='asset')
    created_at= models.DateTimeField(auto_now_add=True)
    modified_at= models.DateTimeField(auto_now_add=True)
    is_assigned= models.BooleanField(default=False)
    quantity= models.IntegerField()
    def __str__(self) -> str:
        return self.name
class EmployeeAssetRequest(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='employeeassetrequest')
    name= models.ForeignKey(Asset,on_delete=models.CASCADE)
    request_urgency= models.TextField()
    quantity= models.IntegerField(default=0)
    status= models.BooleanField(default=False)
    posted_date=models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.request_urgency
class ManagerRequest(models.Model):
    request= models.TextField()
    posted_date=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='managerrequest')
    def __str__(self) -> str:
        return self.request