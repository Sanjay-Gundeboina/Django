from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from .models import EMPLOYEE
from django.views.decorators.csrf import csrf_exempt
def welcome(req):
    return HttpResponse("wellcome user!!")
@csrf_exempt
def reg_user(req):
    # print(req.body)
    data=json.loads(req.body)
    # print(data)
    new_emp=EMPLOYEE.objects.create(
        id=data["id"],
        emp_name=data["name"],
        emp_mob=data["mob"],
        emp_mail=data["email"]
    )
    print(new_emp)
   
    return HttpResponse("user registered sucessfully")

def get_user(req,id):
    emp=EMPLOYEE.objects.get(id=id)
    print(emp.id)
    print(emp.emp_name)
    print(emp.emp_mob)
    print(emp.emp_mail)
    return HttpResponse("user details")

@csrf_exempt
def update_emp(req,emp_id):
    emp=EMPLOYEE.objects.get(id=emp_id)
    print(emp)
    data=json.loads(req.body)
    # print(data)
    for i in data:
        # print(i)
        if i=="name":
            emp.emp_name=data['name']
            emp.save()  
        elif i=="email":
            emp.emp_mail=data['email']
            emp.save()
        elif i=="mbno":
            emp.emp_mob=data['mbno']
            emp.save()
            
    # if data['name']:
    #     emp.emp_name=data['name']
    #     # emp.emp_mail=data['email']
    #     # emp.emp_mob=data['mbno']
    #     emp.save()  
    # if data['email']:
    #     emp.emp_mail=data['email']
    #     emp.save()
    # if data['mbno']:
    #     emp.emp_mob=data['mbno']
    #     emp.save()
   
        
    return HttpResponse("user details updated")