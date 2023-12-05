from django.db import models

# Create your models here.
class Qualification(models.Model):
    name=models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    
