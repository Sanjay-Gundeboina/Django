from django.db import models
from datetime import datetime

# Create your models here.
class DJANGO_USERS(models.Model):
    u_id=models.IntegerField(primary_key=True)
    u_name=models.CharField(max_length=50)
    password=models.CharField(max_length=255)
    u_mob=models.CharField( max_length=10)
    reg_on=models.DateTimeField(blank=True,default=datetime.now())