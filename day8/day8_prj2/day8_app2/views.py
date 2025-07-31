from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import student

def wish(req):
    return HttpResponse("hello user,good evening")

@csrf_exempt
def register_student(req):
    stu_data=json.loads(req.body)
    new_student=student.objects.create(
        std_id=stu_data['id'],
        std_name=stu_data['name'],
        std_course=stu_data['course'],
        std_age=stu_data['age']

    )
    print(stu_data)
    
    return HttpResponse("student registered sucessfully",status=201)

@csrf_exempt
def update_student(req,id):
    stu=student.objects.get(std_id=id)
    data=json.loads(req.body)
    for i in data:
        if i=="id":
            stu.std_id=data['id']
            stu.save()
        elif i=="name":
            stu.std_name=data['name']   
            stu.save()     
        elif i=="course":
            stu.std_course=data['course']
            stu.save()
        elif i=="age":
            stu.std_age=data['age']
            stu.save()
    return HttpResponse("student details updated")
    