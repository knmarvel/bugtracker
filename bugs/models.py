from django.db import models
from datetime import datetime
from django.urls import reverse
from django.template.defaultfilters import slugify

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
        ('New', 'New'),
        ('In Process', 'In Process'),
        ('Done', 'Done'),
        ('Invalid', 'Invalid')
    ]
    title = models.CharField(
        max_length=200
    )
    reported_date = models.DateTimeField(
        default=datetime.now
    )
    completed_date = models.DateTimeField(
        null=True,
        blank=True
    )
    description = models.TextField()
    reported_by = models.ForeignKey(
        MyUser,
        related_name="reported_by", 
        on_delete=models.SET("Deleted user"))
    status = models.CharField(
        max_length = 10,
        choices=TICKET_STATUSES
    )
    assigned_to = models.ForeignKey(
        MyUser,
        related_name="owner",
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    completed_by = models.ForeignKey(
        MyUser,
        related_name="completed_by", 
        null=True,
        blank=True,
        on_delete=models.SET("Deleted user"))
    slug = models.SlugField(
        null=False,
        unique=True,
    )
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("ticket_detail", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    