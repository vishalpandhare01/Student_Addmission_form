from django.db import models
from distutils.command.upload import upload


# Create your models here.
class StudentReg(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)


class AddmisionForm(models.Model):
    photo=models.FileField(upload_to='images',max_length=300,default=None,null=True)
    full_name=models.CharField(max_length=100)
    email=models.EmailField()
    fathare_name=models.CharField(max_length=100)
    Phone_Number=models.IntegerField()
    adhar_number=models.IntegerField()
    Address=models.TextField()
    date=models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=10)