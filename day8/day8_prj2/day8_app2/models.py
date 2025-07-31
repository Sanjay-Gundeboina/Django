from django.db import models

class student(models.Model):
    std_id=models.IntegerField(primary_key=True)
    std_name=models.CharField(max_length=50,null=False,default="std_x")
    std_course=models.CharField(max_length=50,null=False)
    std_age=models.IntegerField()
