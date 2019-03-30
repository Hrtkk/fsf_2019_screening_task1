from django.db import models
from django.contrib.auth import get_user_model
from datetime import date
User = get_user_model()


STATUS_CHOICES = (
            ('Planning', 'Planning'),
            ('Progressing', 'Progressing'),
            ('Done', 'Done'),
        )


class Teams(models.Model):
    title       = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    teamMember  = models.ManyToManyField(
            User,
            through='TeamUserMembership',
            related_name='MemberTeams',
        )
    teamAdmin   = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
            related_name='AdminTeams',
        )
    objects = models.Manager()


class TeamUserMembership(models.Model):
    teamMember  = models.ForeignKey(User, on_delete = models.CASCADE)
    teamName    = models.ForeignKey(Teams, on_delete = models.CASCADE)
    date        = models.DateTimeField()


class Tasks(models.Model):
    title = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    status = models.CharField(max_length=255, choices = STATUS_CHOICES)
    teams = models.ForeignKey(
            Teams,
            on_delete=models.CASCADE,
            related_name='Tasks',
        )
    creator = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
            related_name='TasksAdmin'
        )
    member = models.ManyToManyField(
            User,
            through='TaskUserMembership',
            related_name='TasksMember'
        )
    objects = models.Manager()

    def __str__(self):
        return self.title


class TaskUserMembership(models.Model):
    taskMember  = models.ForeignKey(User, on_delete = models.CASCADE)
    taskName    = models.ForeignKey(Tasks, on_delete = models.CASCADE)
    date        = models.DateTimeField()


class Comments(models.Model):
    comments = models.CharField(max_length=255,)
    author   = models.CharField(max_length=255)
    task     = models.ForeignKey(
            Tasks, 
            related_name='comments',
            on_delete = models.CASCADE
        )
    objects = models.Manager()

