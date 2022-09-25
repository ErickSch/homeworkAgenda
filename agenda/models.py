# erick
# lionelerick54@hotmail.com
# Pass

from django.db import models
from django.utils import timezone




# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=30)
    teacher = models.CharField(max_length=30)


    def __str__(self):
        return self.name

class Homework(models.Model):
    title = models.CharField(max_length=30)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    description = models.TextField()
    # deadline_date = models.DateField(default=timezone.now)
    
    

    def __str__(self):
        return self.title


    
