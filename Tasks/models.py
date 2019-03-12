from django.db import models

# Create your models here.
class Tasks(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    Assignee = models.CharField(max_length=30)
    # Status = models.
    # comments = models.
    # favorite = models.BooleanField()
    
class comments(models.Model):
    comments = models.CharField(max_length=30)
