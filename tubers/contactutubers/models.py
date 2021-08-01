from django.db import models
from datetime import datetime


# Create your models here.
class Contactutubers(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    company_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    detail_message = models.TextField(blank=True)
    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email
