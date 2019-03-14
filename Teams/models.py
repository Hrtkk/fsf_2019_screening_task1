from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Team(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    timestamp = models.DateField(auto_now_add=True, auto_now=False)
    
class TeamList(models.Model):
    Tasks = models.ManyToManyField(Team)
    