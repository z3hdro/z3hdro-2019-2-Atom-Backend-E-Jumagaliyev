from django.shortcuts import render
from django.conf import settings
from users.models import User
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def find_user(request, username):
    if (request.method == 'GET'):
        data = User.objects.all().filter(username__contains = username).values()
        if (len(list(data)) != 0):
            return JsonResponse({'founded user': list(data)})
        else:
            return JsonResponse({'founded user': 'NOT FOUND'})
    return HttpResponseNotAllowed(['GET']) 