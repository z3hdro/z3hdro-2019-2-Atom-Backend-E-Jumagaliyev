from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotAllowed

# Create your views here.
@csrf_exempt
def render_method(request):
    if (request.method == 'GET'):
        return render(request, 'index.html')
    #return JsonResponse({'test':'KEK'})
    return HttpResponseNotAllowed(['GET'])