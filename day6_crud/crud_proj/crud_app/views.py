from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . import users
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
def welcome(req):
    return HttpResponse("wellcome to crud_app")


#READ
user_data=users.user_list
@csrf_exempt
def get_users(req):
    if req.method=="GET":
        if(len(user_data)>0):
            return JsonResponse({"data":user_data})
        else:
            return JsonResponse({"msg":"there are no users"})
    else:
        return HttpResponse("invalid method")

#create
@csrf_exempt
def post_users(req):
    if req.method=="POST":
        reg_data=json.loads(req.body)
        try:
         if reg_data["username"] and reg_data["password"] and reg_data["email"] and reg_data["mobile"]:
            details={
                "id":len(user_data)+1,
                "username":reg_data["username"],
                "password":reg_data["password"],
                "email":reg_data["email"],
                "mobile":reg_data["mobile"]
            }
            user_data.append(details)
            return HttpResponse("data posted sucessfully")
        except:
            return HttpResponse("missing required fields")
 



@csrf_exempt       
def patch_users(req,id):
    if req.method=="PATCH":
        data=json.loads(req.body)
        user_exist=False
        for i in user_data:
            if i["id"]==id:
                user_exist=True
                i["password"]=data["password"]
                return HttpResponse("password updated")
        if user_exist==False:
            return HttpResponse("user not found")
            
    