from django.db import models
from datetime import datetime


# Create your models here.
class HireYoutubers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    utuber_id = models.IntegerField()
    utuber_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    user_id = models.IntegerField(blank=True)
    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email
