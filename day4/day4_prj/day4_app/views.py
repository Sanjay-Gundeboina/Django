from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def user_details(req):
    return JsonResponse({"name":"sanjay","mbno":"7993601901","email":"sanjaygundeboina9@gmail.com"})