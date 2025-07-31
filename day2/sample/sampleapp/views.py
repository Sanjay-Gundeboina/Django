from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
# function based view
def sample(self):
    # return HttpResponse("Hello,Wellcome..!!")
    return JsonResponse({"msg":"app is working","code":"200"})
