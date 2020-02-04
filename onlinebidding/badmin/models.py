from django.db import models

# Create your models here.
class AdminModel(models.Model):
    uname = models.CharField(max_length=30)
    upass = models.CharField(max_length=30)
