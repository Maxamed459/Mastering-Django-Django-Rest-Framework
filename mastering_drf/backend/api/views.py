from django.shortcuts import render
from django.http import JsonResponse
import json



def api_home(request, *args, **kwargs):
    body = request.body # byte string of JSON data
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print(data)
    data['headers'] = dict(request.headers) # request.META
    print(request.headers)
    print(request.GET) # url quey params
    print(request.POST)
    data['params'] = dict(request.GET)
    data['content_type'] = request.content_type
    return JsonResponse(data)
 