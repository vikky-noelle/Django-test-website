from django.db import models

# Create your models here.
class subscribers(models.Model):
    your_email = models.CharField(max_length=45)
