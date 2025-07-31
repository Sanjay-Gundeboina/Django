from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import json
from .serializer import DJANGO_USER_SERIALIZER
from .models import DJANGO_USERS
import bcrypt
# Create your views here.
def reg_user(req):
   try:
    req_data=json.loads(req.body)
    print(req_data)
    password=req_data["password"].encode("utf-8")
    salt=bcrypt.gensalt(12)
    hashed_password=bcrypt.hashpw(password,salt)
    hashed_password=str(hashed_password)
    req_data["password"]=hashed_password
    print(hashed_password)
    
    serialize=DJANGO_USER_SERIALIZER(data=req_data)
    if serialize.is_valid():
        serialize.save()
        return JsonResponse({"msg":"user data saved sucessfully"},status=201)
    else:
        return HttpResponse("error saving")
   except Exception as e:
       return JsonResponse({"error":e})