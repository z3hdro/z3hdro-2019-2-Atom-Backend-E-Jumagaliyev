from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def chat_lists (request):
    if (request.method == 'GET'):
        return JsonResponse({'users':['Kolya','Tolya', 'Shrek']})
    return HttpResponseNotAllowed(['GET'])

@csrf_exempt
def contacts (request):
    if (request.method == 'GET'):
        return JsonResponse({'id-1':'111111', 'id-2':'2222'})
    return HttpResponseNotAllowed(['GET'])