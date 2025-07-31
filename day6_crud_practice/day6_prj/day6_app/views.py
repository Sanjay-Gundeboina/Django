from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . import users
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def wellcome(req):
    return HttpResponse("wellcome to day6 practice")

user_data=users.users_list

@csrf_exempt
def get_users(req):
    if req.method=="GET":
        if len(user_data)>0:
            return JsonResponse({"data":user_data})
        else:
            return JsonResponse({"msg":"there are users"})
    else:
        return HttpResponse("Invalid method")
        
@csrf_exempt    
def post_users(req):
    if req.method=="POST":
        reg_data=json.loads(req.body)
        try:
            if reg_data["username"] and reg_data["password"]:
                details={
                    "id": len(user_data)+1,
                    "username":reg_data["username"],
                    "password":reg_data["password"]
                    
                }
                user_data.append(details)
                return HttpResponse("data posted sucessfully")
        except:
            return HttpResponse("missing required fields")
        
@csrf_exempt
def patch_users(req,id):
    if req.method=="PATCH":
        data=json.loads(req.body)
        user_exits=False
        for i in user_data:
            if i["id"]==id:
                user_exits=True
                i["password"]= data["password"]
                return HttpResponse("password updated")
        if user_exits==False:
            return HttpResponse("user not found")
        
@csrf_exempt
def put_users(req,id):
    if req.method=="PUT":
        data=json.loads(req.body)
        for i in user_data:
            if i["id"]==id:
                i["password"]=data["password"]
                i["username"]=data["username"]
                return HttpResponse("details updated") 
            
@csrf_exempt
def del_users(req,id):
    if req.method=="DELETE":
        user_data.remove(user_data[id])
        return HttpResponse("details deleted")