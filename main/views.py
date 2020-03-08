from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def hello(request):

    info_dict =tuple(request.META.items())
    for k, v in info_dict:
        print("k::%s  v::%s" %(k,v))
    return HttpResponse("hello")
