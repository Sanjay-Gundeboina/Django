from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
# @csrf_exempt
# def wellcome(req):
#     # print(req.method)
#     if req.method=="GET":
#          return HttpResponse(f"opened in {req.method}")
#     elif req.method=="POST":
#         return HttpResponse(f"opened in {req.method}")
#     elif req.method=="PUT":
#         return HttpResponse(f"opened in {req.method}")
#     elif req.method=="PATCH":
#         return HttpResponse(f"opened in {req.method}")
#     else:
#         return HttpResponse(f"opened in {req.method}")

def wish(self):
    return HttpResponse("hello user good morning")

def get_api(req):
    return HttpResponse(f"this is from {req.method} method")
def post_api(req):
    return HttpResponse(f"this is from {req.method} method")
def put_api(req):
    return HttpResponse(f"this is from {req.method} method")
def patch_api(req):
    return HttpResponse(f"this is from {req.method} method")
def del_api(req):
    return HttpResponse(f"this is from del {req.method} method")
