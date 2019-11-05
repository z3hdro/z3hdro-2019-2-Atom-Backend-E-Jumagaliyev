from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def profile (request):
    if (request.method == 'GET'):
        return JsonResponse({'id':'228'})
    return HttpResponseNotAllowed(['GET']) 

@csrf_exempt
def page (request):
    if (request.method == 'GET'):
        return JsonResponse({'id':'228', 'name':'Shrek', 'Surname':'MOE BOLOTO'})
    return HttpResponseNotAllowed(['GET'])
