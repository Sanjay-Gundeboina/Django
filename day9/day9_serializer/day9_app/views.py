from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import USERS
from .serializer import UserSerializer

def hello(req):
    return HttpResponse("hello user, welcome to the django session")

@csrf_exempt
def get_users(req):
    data=json.loads(req.body)
    print(data)
    user=USERS.objects.create(
        user_id=data['id'],
        user_name=data['name'],
        user_email=data['email']                
    )
    return HttpResponse("user details")

@csrf_exempt
def get_user_id(req,id):
    user=USERS.objects.get(user_id=id)
    serialize=UserSerializer(user)
    # print(user)
    return JsonResponse({"data":serialize.data})

def del_user(req,id):
    user=USERS.objects.get(user_id=id)
    user.delete()
    return HttpResponse("user deleted sucessfullt")
