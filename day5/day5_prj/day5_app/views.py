from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

name=""
password=""

@csrf_exempt
def wish(req):
    return JsonResponse({"msg":"hello user wellcome","code":201})

@csrf_exempt
def handle_user_login_data(req):
    if req.method=="POST":
        global name,password
        name=req.POST.get("username")
        password=req.POST.get("password")
        email=req.POST.get("email")
        mbno=req.POST.get("mbno")
        print(name,password,email,mbno)
        if name and password:
            return user_login(name,password)
       
    #     return JsonResponse({"msg":"data submitted sucessfully"})
    # else:
    #     return HttpResponse("data can't submitted ")

# @csrf_exempt
# def handle_user_login_json_data(req):
#     # print(req.body)
#     # print(json.loads(req.body))
#     user_data=json.loads(req.body)
#     # print(user_data["username"])
#     # print(user_data["password"])
#     if user_data["username"] and user_data["password"]:
        
#         return user_login(user_data["username"],user_data["password"])
    
def user_login(u,p):
    if u=="sanjay" and p=="sanju@0":
        return HttpResponse("login sucessdfull")
    else:
        return HttpResponse("invalid credentials")