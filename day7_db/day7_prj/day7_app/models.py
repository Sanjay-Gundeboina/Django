from django.db import models

# Create your models here.
class sampleTable(models.Model):
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    mobile=models.CharField(max_length=50,default=0)
    
# class sample2(models.Model):
#     id=models.IntegerField(primary_key=True)
    
    