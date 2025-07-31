from django.db import models

class CAR(models.Model):
    car_id=models.IntegerField(primary_key=True)
    car_name=models.CharField(max_length=100,null=False)
    car_model=models.IntegerField(null=False)
    

    
