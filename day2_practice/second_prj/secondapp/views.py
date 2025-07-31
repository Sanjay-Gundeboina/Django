from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def second(self):
    return JsonResponse({"msg":"second project executed successfully","code":"200"})
