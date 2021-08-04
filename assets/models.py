from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.enums import Choices
# Create your models here.


class Department(models.Model):
    name= models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    modified_at = models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='department', null=True)

    def __str__(self):
        return self.name

class Asset(models.Model):
    name= models.CharField(max_length=50)
    description= models.TextField()
    image= CloudinaryField('image')
    department= models.ForeignKey('Department',on_delete=models.CASCADE,related_name='asset')
    created_at= models.DateTimeField(auto_now_add=True)
    modified_at= models.DateTimeField(auto_now=True)
    is_assigned= models.BooleanField(default=False)
    quantity= models.IntegerField()

    def __str__(self) -> str:
        return self.name



REQUESTTYPE_CHOICES = (
    ("new_asset", "new_asset"),
    ("repair", "repair"),
    ("replacement", "replacement"),

)


class EmployeeAssetRequest(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='employeeassetrequest')
    name= models.ForeignKey(Asset,on_delete=models.CASCADE)
    type= models.CharField(max_length=50 , choices=REQUESTTYPE_CHOICES,default='new_asset')
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