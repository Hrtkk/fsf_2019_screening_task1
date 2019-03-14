from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Team(models.Model):
    STATUS_TYPE = (
        (1,'Planning'),
        (2,'Progressing'),
        (3,'Done'),
    )
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    assignee = models.CharField(max_length=30)
    status = models.PositiveIntegerField(choices=STATUS_TYPE)
    # add_Comments = models.ManyToManyField(Comments)
    favorite = models.BooleanField(default=False)
    # members = models.ForeignKey()
    timestamp = models.DateField(auto_now_add=True, auto_now=False)
    
class TeamList(models.Model):
    Tasks = models.ManyToManyField(Team)
    