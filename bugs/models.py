from django.db import models
from datetime import datetime

from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    display_name = models.CharField(
        max_length=150,
        null=True,
        blank=True
    )
    REQUIRED_FIELDS = ['display_name']


class Ticket(models.Model):
    TICKET_STATUSES = [
        ('N', 'New'),
        ('P', 'In Progress'),
        ('D', 'Done'),
        ('I', 'Invalid')
    ]
    title = models.CharField(
        max_length=200
    )
    time_of_origin = models.DateTimeField(
        default=datetime.now
    )
    time_of_completion = models.DateTimeField(
        null=True,
        blank=True
    )
    description = models.TextField()
    reported_by = models.ForeignKey(
        MyUser,
        related_name="reporter", 
        on_delete=models.SET("Deleted user"))
    status = models.CharField(
        max_length = 1,
        choices=TICKET_STATUSES
    )
    assigned_to = models.ForeignKey(
        MyUser,
        related_name="owner",
        null=True,
        on_delete=models.SET_NULL)
    completed_by = models.ForeignKey(
        MyUser,
        related_name="completed_by", 
        null=True,
        on_delete=models.SET("Deleted user"))
    
    def __str__(self):
        return self.title
