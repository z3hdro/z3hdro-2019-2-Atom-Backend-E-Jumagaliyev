from django.shortcuts import render
from django.conf import settings
from users.models import User
from users.forms import UserForm
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def create_user(request):
    form = UserForm(request.POST)
    if form.is_valid():
        user = form.save()
        return JsonResponse({
            'Result':'User created',
            'id': user.id
        })
    return JsonResponse({'error': form.errors}, status=400)


@csrf_exempt
def show_all_users(request):
    if request.method == 'GET':
        data = User.objects.all().order_by('id').values()
        return JsonResponse({'result': list(data)})
    return HttpResponseNotAllowed(['GET'])


@csrf_exempt
def find_user(request, username):
    if request.method == 'GET':
        data = User.objects.all().filter(username__contains = username).values()
        if len(list(data)) != 0:
            return JsonResponse({'founded user': list(data)})
        else:
            return JsonResponse({'founded user': 'NOT FOUND'})
    return HttpResponseNotAllowed(['GET'])
