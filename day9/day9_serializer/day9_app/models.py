from django.db import models

class USERS(models.Model):
    user_id=models.IntegerField(primary_key=True)
    user_name=models.CharField(max_length=100,unique=True,null=False)
    user_email=models.CharField(max_length=50,unique=True)