from django.db import models
# Create your models here.
from django.contrib.auth import get_user_model

from datetime import date
User = get_user_model()


class TeamsList(models.Model):
    id = models.IntegerField(primary_key=True,unique=True)


class Teams(models.Model):
    title       = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    admin       = models.EmailField()
    teamMember  = models.ManyToManyField(User, through='Membership')
    TeamsList   = models.ForeignKey(
        TeamsList,
        on_delete=models.CASCADE,
        related_name='teams'
    )


class Membership(models.Model):
    teamMember  = models.ForeignKey(User, on_delete=models.CASCADE)
    teamName    = models.ForeignKey(Teams, on_delete=models.CASCADE)
    date        = models.DateTimeField()


