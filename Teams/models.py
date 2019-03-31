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
    # Team model
    title       = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    # many to many relationship with through field so that teamms can be accessed from user objects 
    teamMember  = models.ManyToManyField(
            User,
            through='TeamUserMembership',
            related_name='MemberTeams',
        )
    # foreign key to user as for a there can only be one team admin
    teamAdmin   = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
            related_name='AdminTeams',
        )
    # object manager for providing extra method
    objects = models.Manager()


class TeamUserMembership(models.Model):
    teamMember  = models.ForeignKey(User, on_delete = models.CASCADE)
    teamName    = models.ForeignKey(Teams, on_delete = models.CASCADE)
    date        = models.DateTimeField(auto_now=True, null=True)
    objects = models.Manager()


class Tasks(models.Model):
    # Task model 
    title = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    status = models.CharField(max_length=255, choices = STATUS_CHOICES)
    # foreign relationship for task to team as each task will have only one parent team
    teams = models.ForeignKey(
            Teams,
            on_delete=models.CASCADE,
            related_name='Tasks',
        )
    # foreign key to User
    creator = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
            related_name='TasksAdmin'
        )
    # Many to many relationship between user and task as there can be 
    # many users associated with task and many task can be associated with user
    member = models.ManyToManyField(
            User,
            through='TaskUserMembership',
            related_name='TasksMember'
        )
    objects = models.Manager()

    def __str__(self):
        # string thunder for showing title as object
        return self.title


class TaskUserMembership(models.Model):
    # Task and user relationship 
    taskMember  = models.ForeignKey(User, on_delete = models.CASCADE)
    taskName    = models.ForeignKey(Tasks, on_delete = models.CASCADE)
    date        = models.DateTimeField(auto_now=True, null=True)


class Comments(models.Model):
    # comments model
    comments = models.CharField(max_length=255,)
    author   = models.CharField(max_length=255)
    task     = models.ForeignKey(
            Tasks, 
            related_name='comments',
            on_delete = models.CASCADE
        )
    objects = models.Manager()

