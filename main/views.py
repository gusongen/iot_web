from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.
def hello(request, *args):
    info_dict = tuple(request.META.items())
    for k, v in info_dict:
        print("k::%s  v::%s" % (k, v))
    return JsonResponse({'mag': "ok", 'status': 200})


def test(request, key):
    location = request.GET.get('location')
    language = request.GET.get("language")
    info_dict = tuple(request.META.items())
    for k, v in info_dict:
        print("k::%s  v::%s" % (k, v))
    return JsonResponse({'mag': "ok", 'status': 200})
