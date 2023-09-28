from django.db import models


# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=25,null=True)
    email=models.EmailField(max_length=60,null=True)
    password=models.CharField(max_length=12,null=True)
    phone=models.CharField(max_length=10,null=True)
    gender=models.CharField(max_length=1,null=True)
    city=models.CharField(max_length=2,null=True)
    Img=models.ImageField(upload_to="media",null=True)
    Resume=models.FileField(upload_to="media",null=True)

    def __str__(self):
        return self.name




class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15, unique=True)
    otp = models.CharField(max_length=6, blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.email

