from django.db import models

# Create your models here.
from django.db import models

class Course(models.Model):
    course_title=models.CharField(max_length=100)
    course_disc=models.CharField(max_length=300)
