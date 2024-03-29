from django.db import models
from django.utils import timezone
import math
# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True,max_length=30,blank=False)
    password = models.CharField(max_length=15)
    role = models.CharField(max_length=15)
    is_active = models.BooleanField(default=False)
    is_varify = models.BooleanField(default=False)
    otp = models.IntegerField(default=456)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Admin(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    contact_no = models.CharField(max_length=10)
    pic = models.FileField(upload_to="media/upload", default="media/chairman-default.png")
    

    def __str__(self):
        return self.firstname

class Member(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=30)

    def __str__(self):
        return self.firstname