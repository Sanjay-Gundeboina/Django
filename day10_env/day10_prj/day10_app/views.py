from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from .models import CAR
from django.views.decorators.csrf import csrf_exempt
from .serializer import CarSerializer

def welcome(req):
    return HttpResponse("hello welcome to env_app")

@csrf_exempt
def create_cars(req):
    data=json.loads(req.body)
    print(data)
    cars=CAR.objects.create(
        car_id= data['car-id'],
        car_name = data['car-name'],
        car_model=data['car-model']      
    )
    # print(cars)
    return HttpResponse("new car data added sucessfully",status=201)

@csrf_exempt
def get_cars(req,id):
    try:
        cars=CAR.objects.get(car_id=id)
        new_car=CarSerializer(cars)
        return JsonResponse({"data":new_car.data})
    except Exception as error:
        return HttpResponse("error:",f"{error}")

@csrf_exempt
def update_car(req,id):
    data=json.loads(req.body)
    car=CAR.objects.get(car_id=id)
    print(data)
    for i in data:
        if i=="id":
            car.car_id=data['id']
            car.save()
        elif i=="name":
            car.car_name=data['name']
            car.save()
        elif i== "model":
            car.car_model=data['model']
            car.save()
    return HttpResponse("car details updated",status=201)


@csrf_exempt
def delete_car(req,id):
    car=CAR.objects.get(car_id=id)
    car.delete()
    return HttpResponse("car deleted sucess fully")
    