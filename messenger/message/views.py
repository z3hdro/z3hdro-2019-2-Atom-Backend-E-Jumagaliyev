from django.shortcuts import render
from message.models import Message
from message.forms import MessageForm
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def create_message(request):
    form = MessageForm(request.POST)
    if form.is_valid():
        message = form.save()
        return JsonResponse({
            'Result':'Message created',
            'id': message.id
        })
    return JsonResponse({'error': form.errors}, status=400, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def show_all_messages(request):
    if request.method == 'GET':
        data = Message.objects.all().order_by('id').values()
        return JsonResponse({'result': list(data)})
    return HttpResponseNotAllowed(['GET'])

@csrf_exempt
def read_message(request):
    if request.method == 'GET':
        message = request.GET.get('message_id')
        data = Message.objects.filter(id=message).values()
        if len(list(data)) != 0:
            return JsonResponse({
                'message': list(data)
            })
        else:
            return JsonResponse({'Error':'Such message is not found!'})
    return HttpResponseNotAllowed(['GET'])