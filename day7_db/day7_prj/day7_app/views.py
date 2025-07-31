from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import sampleTable
# Create your views here.

def wish(req):
    return HttpResponse("wellcome to the app")

def get_users(req):
    all_users=sampleTable.objects.all()
    for i in all_users:
        print(i.name)
    return HttpResponse("getting users")