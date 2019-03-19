# from django.db import models
# from Teams.models import Teams
# from django.contrib.auth import get_user_model
# # Create your models here.
# User = get_user_model()


# class Tasks(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)
#     teams = models.ForeignKey(
#         Teams,
#         on_delete=models.CASCADE,
#         related_name='Tasks',
#     )
#     # STATUS_CHOICES = (
#         ('Planning', 'Planning'),
#         ('Progressing', 'Progressing'),
#         ('Done', 'Done'),
#     )
#     status = models.CharField(max_length=255, choices=STATUS_CHOICES)
#     creator = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name='Teams'
#     )
