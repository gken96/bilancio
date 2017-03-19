from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils import timezone


class buy_list(models.Model):
    creator = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

    

    def __str__(self):
        return self.title
